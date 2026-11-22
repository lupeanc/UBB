import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Sequential {

    public void process(String folderPath, ResultList resultList)
            throws IOException {

        for (int i = 1; i <= 10; i++) {

            String filePath = folderPath + "/project" + i + ".txt";

            try (BufferedReader reader =
                         new BufferedReader(new FileReader(filePath))) {

                String line;

                while ((line = reader.readLine()) != null) {

                    String[] parts = line.split(",");

                    int id = Integer.parseInt(parts[0].trim());
                    int grade = Integer.parseInt(parts[1].trim());

                    resultList.addOrUpdate(id, grade);
                }
            }
        }
    }
}
