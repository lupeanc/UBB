
import java.io.*;
import java.util.*;

public class Main {

    // Matrix F
    private static int[][] f;

    // Convolutional Matrix
    private static int[][] c;

    // Result matrix
    private static int[][] v;
    private static int n, m, k;

    private static final String matrixFFilePath = "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\MatrixF.txt";
    private static final String convMatrixFilePath = "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\ConvolutionM.txt";
    private static final String outputFilePath = "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L1\\L1Java\\output.txt";

    /**
     * Read matrices from already existing files
     * @throws IOException
     */
    private static void readMatrices() throws IOException {
        try (Scanner sc = new Scanner(new File(matrixFFilePath))) {
            List<int[]> rows = new ArrayList<>();

            while (sc.hasNextLine()) {
                String line = sc.nextLine().trim();

                if (line.isEmpty()) {
                    continue;
                }

                String[] values = line.split(" ");
                int[] row = new int[values.length];

                for (int j = 0; j < values.length; j++) {
                    row[j] = Integer.parseInt(values[j]);
                }

                rows.add(row);
            }

            n = rows.size();
            m = rows.getFirst().length;
            f = new int[n][m];

            for (int i = 0; i < n; i++) {
                if (rows.get(i).length != m) {
                    throw new IllegalArgumentException(
                            "MatrixF.txt has inconsistent row lengths");
                }

                f[i] = rows.get(i);
            }
        }

        try (Scanner sc = new Scanner(new File(convMatrixFilePath))) {
            List<int[]> rows = new ArrayList<>();

            while (sc.hasNextLine()) {
                String line = sc.nextLine().trim();

                if (line.isEmpty()) {
                    continue;
                }

                String[] values = line.split(" ");
                int[] row = new int[values.length];

                for (int j = 0; j < values.length; j++) {
                    row[j] = Integer.parseInt(values[j]);
                }

                rows.add(row);
            }

            k = rows.size();

            // not sure if needed
//            if (k % 2 == 0) {
//                throw new IllegalArgumentException(
//                        "Kernel size must be a positive odd number");
//            }

            c = new int[k][k];

            for (int i = 0; i < k; i++) {
                if (rows.get(i).length != k) {
                    throw new IllegalArgumentException(
                            "Convolution matrix must be square");
                }

                c[i] = rows.get(i);
            }
        }

        v = new int[n][m];
    }

    private static int getValueOfCurrentCell(int i, int j) {
        // if i or j are out of bounds, return the same value that exists on the same
        // row/column inside the matrix

        // so, if i=-1, then the value at i=0 is taken
        // if i>=n, then the value at i=n is taken
        i = Math.max(0, Math.min(i, n - 1));
        j = Math.max(0, Math.min(j, m - 1));

        return f[i][j];
    }

    private static void calculateCell(int i, int j) {
        int sum = 0;
        int radius = k / 2;

        for (int ki = 0; ki < k; ki++) {
            for (int kj = 0; kj < k; kj++) {
                // get equivalent in F to current C elem
                int currentValueInF = getValueOfCurrentCell(
                        // - radius so we center c around the ij elem in F
                        i + ki - radius,
                        j + kj - radius
                );

                sum += currentValueInF * c[ki][kj];
            }
        }

        v[i][j] = sum;
    }

    private static void sequential() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                calculateCell(i, j);
            }
        }
    }

    private static int[][] copyMatrix(int[][] matrix) {
        int[][] copy = new int[matrix.length][];

        for (int i = 0; i < matrix.length; i++) {
            copy[i] = matrix[i].clone();
        }

        return copy;
    }

    private static boolean validate(int[][] expected, int[][] actual) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (expected[i][j] != actual[i][j]) {
                    System.out.println(
                            "Incorrect result at [" + i + "][" + j + "]"
                    );
                    System.out.println(
                            "Expected: " + expected[i][j]
                                    + ", actual: " + actual[i][j]
                    );

                    return false;
                }
            }
        }

        return true;
    }

    private static void writeMatrix(int[][] matrix) throws IOException {
        try (PrintWriter out = new PrintWriter(outputFilePath)) {
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

    private static void parallel(int p, String mode) throws InterruptedException {
        if (p <= 0) {
            throw new IllegalArgumentException(
                    "Number of threads must be positive");
        }

        MyThread[] threads = new MyThread[p];

        for (int tid = 0; tid < p; tid++) {
            threads[tid] = new MyThread(tid, p, mode);
            threads[tid].start();
        }

        for (int tid = 0; tid < p; tid++) {
            threads[tid].join();
        }
    }

    // Supported modes:
    // sequential, horizontal, vertical
    public static void main(String[] args) throws IOException, InterruptedException {

        readMatrices();

        String mode = args.length > 0 ? args[0] : "sequential";
        int p = args.length > 1 ? Integer.parseInt(args[1]) : 4;

        // Compute the reference result outside the timed section.
        sequential();
        int[][] expected = copyMatrix(v);

        // Each run starts with a fresh output matrix.
        v = new int[n][m];

        long start = System.nanoTime();

        if (mode.equals("sequential")) {
            sequential();
        } else {
            parallel(p, mode);
        }

        long end = System.nanoTime();

        double timeMs = (end - start) / 1_000_000.0;

        if (!validate(expected, v)) {
            throw new RuntimeException("Verification failed!");
        }

        writeMatrix(v);

        System.out.println(timeMs);
    }

    private static class MyThread extends Thread {
        private final int tid;
        private final int p;
        private final String mode;

        public MyThread(int tid, int p, String mode) {
            this.tid = tid;
            this.p = p;
            this.mode = mode;
        }

        @Override
        public void run() {
            switch (mode) {
                case "horizontal":
                    horizontal();
                    break;

                case "vertical":
                    vertical();
                    break;

                default:
                    throw new IllegalArgumentException(
                            "Unknown parallel mode: " + mode);
            }
        }

        private void horizontal() {
            int begin = getStart(n, p, tid);
            int end = getEnd(n, p, tid);

            for (int i = begin; i < end; i++) {
                for (int j = 0; j < m; j++) {
                    calculateCell(i, j);
                }
            }
        }

        private void vertical() {
            int begin = getStart(m, p, tid);
            int end = getEnd(m, p, tid);

            for (int i = 0; i < n; i++) {
                for (int j = begin; j < end; j++) {
                    calculateCell(i, j);
                }
            }
        }
    }
}
