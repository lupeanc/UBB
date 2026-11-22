import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {

        String folderPath = "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L4\\L4Java\\data";

        long startTime = System.nanoTime();

        ResultList resultList = new ResultList();
        Sequential processor = new Sequential();

        try {
            // Read all project files.
            processor.process(folderPath, resultList);

            // Write the final results.
            try (BufferedWriter writer =
                         new BufferedWriter(new FileWriter("ResultsSequential.txt"))) {

                resultList.writeToFile(writer);
            }

        } catch (IOException e) {
            e.printStackTrace();
            return;
        }

        long endTime = System.nanoTime();

        double executionTime =
                (endTime - startTime) / 1_000_000.0;

        System.out.println(executionTime);
    }
}
