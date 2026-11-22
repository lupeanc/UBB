import java.util.Random;
import java.util.Vector;

public class Main {

    static int n = 1000;

    static int[] a = new int[n];
    static int[] b = new int[n];
    static int[] c = new int[n];

//    static Vector<Integer> a = new Vector<>();
//    static Vector<Integer> b = new Vector<>();
//    static Vector<Integer> c = new Vector<>();

    static void allocateVectors() {
        Random randomNumber = new Random();

        for (int i = 0; i < n; i++) {
            a[i] = randomNumber.nextInt(n);
            b[i] = randomNumber.nextInt(n);

//            a.set(i, randomNumber.nextInt(n));
//            b.set(i, randomNumber.nextInt(n));
        }
    }

    static void calculateC() {
        for (int i = 0; i < n; i++) {
            c[i] = a[i] + b[i];
//            c.set(i, a.get(i) + b.get(i));
        }
    }

    public static void main(String[] args) {
        long startTime = System.nanoTime();

        allocateVectors();
        calculateC();

        long endTime = System.nanoTime();

        double duration = (endTime - startTime) / 1_000_000.0;

        System.out.println(duration);
    }
}