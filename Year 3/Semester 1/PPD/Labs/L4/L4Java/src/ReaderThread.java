
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.List;

// producer threads
public class ReaderThread extends Thread {

    // path to files
    private final List<String> files;

    // the shared queue for all threads
    private final RecordQueue queue;

    public ReaderThread(
            List<String> files,
            RecordQueue queue) {

        this.files = files;
        this.queue = queue;
    }

    @Override
    public void run() {

        for (String file : files) {

            try (BufferedReader reader =
                         new BufferedReader(new FileReader(file))) {

                String line;

                while ((line = reader.readLine()) != null) {

                    String[] parts = line.split(",");

                    int id = Integer.parseInt(parts[0].trim());
                    int grade = Integer.parseInt(parts[1].trim());

                    queue.addRecordToQueue(new StudentRecord(id, grade));
                }
            } catch (Exception e){
                System.out.println("Error while reading file " + files.getFirst());
            }
        }
    }
}
