import java.util.Random;

public class Main {
    public static int N = 1000000;
    private static Random random = new Random();
    // nb threads
    private static int P = 2;

    private static void validateSum(double[] a,  double[] b, double[] c) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] + b[i] != c[i]) {
                throw new RuntimeException("Sum not correct!");
            }
        }
    }

    private static void sumDouble(double[] a, double[] b, double[] c) {
        if (a.length != b.length || c.length != a.length) {
           throw new RuntimeException("Arrays are not equal");
        }

        for (int i = 0; i < a.length; i++) {
            c[i] = a[i] + b[i];
        }
    }

    private static void assignVectors(double[] a) {
        for (int i = 0; i < a.length; i++) {
            a[i] = random.nextDouble();
        }
    }

    private static void sumBlocks(double[] a, double[] b, double[] c) throws InterruptedException {
        if (a.length != b.length || c.length != a.length) {
            throw new RuntimeException("Arrays are not equal");
        }

        int size = N/P;
        int r = N%P;

        int begin=0;
        int end = size;

        MyThread[] threads = new MyThread[P];

        for(int tid=0; tid<P; tid++){
            if(r>0){
                end+=1;
                r-=1;
            }

            threads[tid] = new MyThread(a, b, c, begin, end);
            threads[tid].start();

            begin = end;
            end = begin+size;
        }

        for(int tid=0; tid<P; tid++){
            threads[tid].join();
        }
    }

    private static void sumBlocksCyclic(double[] a, double[] b, double[] c) throws InterruptedException {
        if (a.length != b.length || c.length != a.length) {
            throw new RuntimeException("Arrays are not equal");
        }

        int size = N/P;

        int begin=0;
        int end = size;

        MyThreadCyclic[] threads = new MyThreadCyclic[P];

        for(int tid=0; tid<P; tid++){

            threads[tid] = new MyThreadCyclic(a, b, c, P, tid);
            threads[tid].start();

            begin = end;
            end = begin+size;
        }

        for(int tid=0; tid<P; tid++){
            threads[tid].join();
        }
    }

	public static void main(String[] args) throws InterruptedException {
        double[] a = new double[N];
        double[] b = new double[N];
        double[] c = new double[N];

//        a[0] = 1.0;
//        b[0] = 2.0;

        assignVectors(a);
        assignVectors(b);

        long t1 = System.nanoTime();
        sumDouble(a, b, c);
        long t2 = System.nanoTime();

        long t3 = System.nanoTime();
        sumDouble(a, b, c);
        long t4 = System.nanoTime();

        long t5= System.nanoTime();
        sumDouble(a, b, c);
        long t6 = System.nanoTime();

        double t1_t2 = (t2 - t1) / 1000000f;
        double t3_t4 = (t4 - t3) / 1000000f;
        double t5_t6 = (t6 - t5) / 1000000f;

        validateSum(a, b, c);

        System.out.println("Time of sum: " + t1_t2);
        System.out.println("Time of sum: " + t3_t4);
        System.out.println("Time of sum: " + t5_t6);

    }
}