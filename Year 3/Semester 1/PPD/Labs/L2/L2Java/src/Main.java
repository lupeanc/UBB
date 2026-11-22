
import java.io.*;
import java.util.*;

public class Main {

    // Matrix F
    private static double[][] f;

    // Convolutional Matrix
    private static double[][] c;

//    private static int[] previousRow;
//    private static int[] currentRow;
//    private static int[] nextRow;
    private static int n, m, k;

    private static final String matrixFFilePath = "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\MatrixF.txt";
    private static final String convMatrixFilePath = "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\ConvolutionM.txt";
    private static final String outputFilePath = "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\output.txt";
    private static final String sequentialOutputFilePath = "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L2\\L2Java\\src\\sequential_output.txt";
    /**
     * Read matrices from already existing files
     * @throws IOException
     */
    private static void readMatrices() throws IOException {
        try (Scanner sc = new Scanner(new File(matrixFFilePath))) {
            List<double[]> rows = new ArrayList<>();

            while (sc.hasNextLine()) {
                String line = sc.nextLine().trim();

                if (line.isEmpty()) {
                    continue;
                }

                String[] values = line.split(" ");
                double[] row = new double[values.length];

                for (int j = 0; j < values.length; j++) {
                    row[j] = Double.parseDouble(values[j]);
                }

                rows.add(row);
            }

            n = rows.size();
            m = rows.getFirst().length;
            f = new double[n][m];

            for (int i = 0; i < n; i++) {
                if (rows.get(i).length != m) {
                    throw new IllegalArgumentException(
                            "MatrixF.txt has inconsistent row lengths");
                }

                f[i] = rows.get(i);
            }

//            previousRow = new int[m];
//            currentRow = new int[m];
//            nextRow = new int[m];
        }

        try (Scanner sc = new Scanner(new File(convMatrixFilePath))) {
            List<double[]> rows = new ArrayList<>();

            while (sc.hasNextLine()) {
                String line = sc.nextLine().trim();

                if (line.isEmpty()) {
                    continue;
                }

                String[] values = line.split(" ");
                double[] row = new double[values.length];

                for (int j = 0; j < values.length; j++) {
                    row[j] = Double.parseDouble(values[j]);
                }

                rows.add(row);
            }

            k = rows.size();

            c = new double[k][k];

            for (int i = 0; i < k; i++) {
                if (rows.get(i).length != k) {
                    throw new IllegalArgumentException(
                            "Convolution matrix must be square");
                }

                c[i] = rows.get(i);
            }
        }

    }

    private static double calculateCell(int j, double[] previousRow, double[] currentRow, double[] nextRow) {
        double sum = 0;
        int index = j-1;

        for (int ki = 0; ki < k; ki++) {
            int col = Math.max(0, Math.min(index, m - 1));

            sum += previousRow[col] * c[0][ki];
            sum += currentRow[col] * c[1][ki];
            sum += nextRow[col] * c[2][ki];

            index++;
        }

        return sum;
    }

    private static void sequential() {
        double[] previousRow = f[0].clone();
        double[] currentRow = f[0].clone();
        double[] nextRow = new double[m];

        for (int i = 0; i < n; i++) {
            if(i < n-1){
                nextRow = f[i+1].clone();
            }

            for (int j = 0; j < m; j++) {
                f[i][j] = calculateCell(j, previousRow, currentRow, nextRow);
            }

            previousRow = currentRow;
            currentRow = nextRow;
        }

    }

    private static boolean validate() {

        try (Scanner sc = new Scanner(new File(sequentialOutputFilePath))) {
            List<double[]> rows = new ArrayList<>();

            while (sc.hasNextLine()) {
                String line = sc.nextLine().trim();

                if (line.isEmpty()) {
                    continue;
                }

                String[] values = line.split(" ");
                double[] row = new double[values.length];

                for (int j = 0; j < values.length; j++) {
                    row[j] = Double.parseDouble(values[j]);
                }
                rows.add(row);
            }

            if (rows.size() != n) {
                System.out.println("Output matrix has inconsistent row lengths");
                return false;
            }

            for(int i = 0; i < n; i++){
                if(!Arrays.equals(f[i], rows.get(i))){
                    System.out.println("Incorrect result at row " + i);
                    return false;
                }
            }

        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        return true;
    }

    private static void writeMatrix(double[][] matrix, String filePath) throws IOException {
        try (PrintWriter out = new PrintWriter(filePath)) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (j > 0) {
                        out.print(" ");
                    }

                    out.print(matrix[i][j]);
                }

                out.println();
            }
        }
    }

    private static int getStart(int rows, int p, int tid) {
        // if rows is not div by p
        // all threads with id < rows%p get an extra row
        // which we add to the starting position
        // so, if rows % p = 2 =>
        // tid-0: add one extra row to the computation, but since start=0, result=0
        // tid-1: added one extra row to the computation for tid-0, so start = +1
        // tid-2: added one extra row for tid-1 AND the one extra row from tid-0, so start = +2
        int rowsProcessedByDefault = tid * (rows / p);
        int extraRowsFromPriorThreads = Math.min(tid, rows % p);
        int startPosition = rowsProcessedByDefault + extraRowsFromPriorThreads;

        return startPosition;
    }

    private static int getEnd(int rows, int p, int tid) {
        // from starting point, add default amount of rows (rows / p)
        // and, if thread has an extra row, add it to the final endPosition
        int endPosition = getStart(rows, p, tid) + rows / p;

        boolean hasExtraRow = tid < rows % p;
        if (hasExtraRow) {
            endPosition++;
        }

        return endPosition;
    }

    private static void parallel(int p) throws InterruptedException {
        if (p <= 0) {
            throw new IllegalArgumentException(
                    "Number of threads must be positive");
        }

        double[] previousRow;
        double[] currentRow;
        double[] nextRow;
        double[] endRow;

        MyThread[] threads = new MyThread[p];

        for (int tid = 0; tid < p; tid++) {
            int begin = getStart(n, p, tid);
            int end = getEnd(n, p, tid);

            if(begin == 0){
                previousRow = f[0].clone();
            } else {
                previousRow = f[begin-1].clone();
            }

            currentRow = f[begin].clone();

            // take the next empty row if it exists, if not, just copy the last row
            nextRow = f[Math.min(begin + 1, n - 1)].clone();

            if(end < n){
                // copy the first following row that isn't being processed
                // by the current thread since we're modifying f as we're going
                endRow = f[end].clone();
            } else {
                // if the end is out of bounds
                // copy the last row of n
                endRow = f[n-1].clone();
            }

            threads[tid] = new MyThread(tid, p, begin, end, previousRow, currentRow, nextRow, endRow);
        }

        for (int tid = 0; tid < p; tid++) {
            threads[tid].start();
        }

        for (int tid = 0; tid < p; tid++) {
            threads[tid].join();
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException {

        readMatrices();

        String mode = args.length > 0 ? args[0] : "sequential";
        int p = args.length > 1 ? Integer.parseInt(args[1]) : 2;

//         Compute the reference result outside the timed section.
        sequential();
        writeMatrix(f, sequentialOutputFilePath);

        // reset variables
        readMatrices();

//        mode = "sequential";
        long start = System.nanoTime();

        if (mode.equals("sequential")) {
            sequential();
        } else {
            parallel(p);
        }

        long end = System.nanoTime();

        double timeMs = (end - start) / 1_000_000.0;

        if (!validate()) {
            throw new RuntimeException("Verification failed!");
        }

        writeMatrix(f, outputFilePath);

        System.out.println(timeMs);
    }

    private static class MyThread extends Thread {
        private final int tid;
        private final int p;

        int begin;
        int end;

        double[] previousRow;
        double[] currentRow;
        double[] nextRow;
        double[] endRow;

        public MyThread(int tid, int p, int begin, int end, double[] previousRow, double[] currentRow, double[] nextRow, double[] endRow) {
            this.tid = tid;
            this.p = p;
            this.begin = begin;
            this.end = end;
            this.previousRow = previousRow;
            this.currentRow = currentRow;
            this.nextRow = nextRow;
            this.endRow = endRow;
        }

        @Override
        public void run() {
            for (int i = this.begin; i < this.end; i++) {
                for (int j = 0; j < m; j++) {
                    f[i][j] = calculateCell(j, previousRow,  currentRow, nextRow);
                }

                this.previousRow = this.currentRow;
                this.currentRow = this.nextRow;

                // + 2 because we are gonna have i+1 on the next run
                if(i + 2 < end){
                    this.nextRow = f[i+2].clone();
                }
                else {
                    this.nextRow = this.endRow;
                }

            }
        }

    }
}
