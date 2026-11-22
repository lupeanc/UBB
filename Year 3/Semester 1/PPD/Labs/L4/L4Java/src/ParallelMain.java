
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ParallelMain {

    public static boolean testResults(ResultList sequentialResults, ResultList parallelResults) throws IOException {
        return sequentialResults.equals(parallelResults);
    }

    public static void main(String[] args) throws Exception {

        // total threads
        if(args.length!=2){
            System.err.println("Not enough arguments.");
            return;
        }

        int p = Integer.parseInt(args[0]);

        // reader threads
        int p_r = Integer.parseInt(args[1]);

        // worker threads
        int p_w = p - p_r;

        String folderPath = "C:\\Users\\Clayton\\Uni\\Year 3\\Semester 1\\PPD\\Labs\\L4\\L4Java\\data";

        // Sequential exec
        ResultList resultListSequential = new ResultList();
        Sequential processor = new Sequential();

        processor.process(folderPath, resultListSequential);

        // declare shared vars
        ResultList resultList = new ResultList();
        RecordQueue queue = new RecordQueue();

        long startTime = System.nanoTime();

        // Divide the 10 files between the readers
        // so a list of the lists of files for each reader (1 list -> 1 reader)
        List<List<String>> readerFiles = new ArrayList<>();

        // declare the lists
        for (int i = 0; i < p_r; i++) {
            readerFiles.add(new ArrayList<>());
        }

        // split the lists
        for (int i = 1; i <= 10; i++) {

            String filename =
                    folderPath + "/project" + i + ".txt";

            // every reader gets 1 list every single turn
            // p_r = 3
            // so for 1 -> reader 0 gets 1.txt, 4.txt, etc
            // 1 -> 2.txt
            // 2 -> 3.txt
            readerFiles.get((i - 1) % p_r).add(filename);
        }

        // Create and start workers
        WorkerThread[] workers = new WorkerThread[p_w];

        for (int i = 0; i < p_w; i++) {
            workers[i] = new WorkerThread(queue, resultList);
            workers[i].start();
        }

        // Create and start the additional readers
        // MAIN THREAD IS ALOS A READER => p_r - 1
        ReaderThread[] readers = new ReaderThread[p_r - 1];

        for (int i = 0; i < p_r - 1; i++) {

            readers[i] = new ReaderThread(
                    readerFiles.get(i + 1),
                    queue
            );

            readers[i].start();
        }

        // The main thread acts as the "first" reader (it gets the first batch of files)
        ReaderThread mainReader = new ReaderThread(
                readerFiles.getFirst(),
                queue
        );

        mainReader.run();

        // Wait until all additional readers finish before
        // sending over the termination record
        for (ReaderThread reader : readers) {
            reader.join();
        }

        // All records have now been added to the queue
        // Send the termination record to each worker
        for (int i = 0; i < p_w; i++) {
            queue.addRecordToQueue(StudentRecord.createFinalRecord());
        }

        // Wait until all workers finish.
        for (WorkerThread worker : workers) {
            worker.join();
        }

        // Write the final result.
        try (BufferedWriter writer =
                     new BufferedWriter(new FileWriter("Results.txt"))) {

            resultList.writeToFile(writer);
        }

        long endTime = System.nanoTime();

        double executionTime =
                (endTime - startTime) / 1_000_000.0;

        if(!testResults(resultListSequential, resultList)){
            System.err.println("Test failed. Results from sequential differ from results from parallel.");
        }

        System.out.println(executionTime);
    }
}
