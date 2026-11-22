import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Random;

public class Main {
    private static int n=5, m=5, k=3;
    private static Random rand = new Random();

    private static void generateFMatrix(int n, int m){
        try (PrintWriter out = new PrintWriter("C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\MatrixF.txt")) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    out.print(rand.nextInt()%100);
                    if(j<m-1){
                        out.print(" ");
                    }
                }
                out.println();
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    private static void generateConvolutionMatrix(int k){
        try (PrintWriter out = new PrintWriter("C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\ConvolutionM.txt")) {
            for (int i = 0; i < k; i++) {
                for (int j = 0; j < k; j++) {

                    out.print(rand.nextInt()%10);
                    if(j<k-1){
                        out.print(" ");
                    }
                }
                out.println();
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        if(args.length==3){
            n = Integer.parseInt(args[0]);
            m = Integer.parseInt(args[1]);
            k = Integer.parseInt(args[2]);
        }

//        n=10;
//        m=10;
//        k=3;
    
        generateFMatrix(n, m);
        generateConvolutionMatrix(k);
        System.out.println("Generated Matrices");

    }
}