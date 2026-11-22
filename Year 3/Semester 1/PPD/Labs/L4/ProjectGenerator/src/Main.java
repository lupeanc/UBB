
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class Main {

    static final String DATA_FILE_PATH =
            "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L4\\L4Java\\data\\";

    static Random random = new Random();

    public static void main(String[] args) throws IOException {

        for (int i = 1; i <= 10; i++) {

            String filename = DATA_FILE_PATH + "project" + i + ".txt";

            try (BufferedWriter writer =
                         new BufferedWriter(new FileWriter(filename))) {

                int numberOfGrades = random.nextInt(31) + 70;

                for (int j = 0; j < numberOfGrades; j++) {

                    int studentID = random.nextInt(100) + 1;
                    int grade = random.nextInt(10) + 1;

                    writer.write(studentID + "," + grade);
                    writer.newLine();
                }
            }
        }

        System.out.println("Project files generated!");
    }
}
