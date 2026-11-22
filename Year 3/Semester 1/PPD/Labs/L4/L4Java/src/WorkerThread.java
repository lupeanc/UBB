// consumer threads
public class WorkerThread extends Thread {

    // shared record queue and shared result list (letter = only among workers)
    private final RecordQueue queue;
    private final ResultList resultList;

    public WorkerThread(RecordQueue queue, ResultList resultList) {
        this.queue = queue;
        this.resultList = resultList;
    }

    @Override
    public void run() {

        try {
            while (true) {

                StudentRecord record = queue.dequeueRecord();

                // Check whether this is a termination signal.
                if (record.checkAllRecordsHaveBeenRead()) {
                    break;
                }

                resultList.addOrUpdate(
                        record.getId(),
                        record.getGrade()
                );
            }

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
