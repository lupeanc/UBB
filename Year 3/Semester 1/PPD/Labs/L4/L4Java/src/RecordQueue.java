
import java.util.concurrent.Semaphore;

public class RecordQueue {

    private static class Node {
        StudentRecord record;
        Node next;

        Node(StudentRecord record) {
            this.record = record;
            this.next = null;
        }
    }

    // first elem in a queue to be dealt with
    private Node head;

    // where elems will be added
    private Node tail;

    // semaphores
    // mutex - used when modifying the list
    // items - used to count how many items to process
    //      => every reader thread increases the permits
    //      => every worker thread decreases the permits
    // why? to allow reader threads and worker threads to work simultaneously
    // this way we dont have to wait for the readers to finish adding the records before processing them
    private final Semaphore mutex = new Semaphore(1);
    private final Semaphore items = new Semaphore(0);

    public RecordQueue() {
        head = null;
        tail = null;
    }

    // Called by reader threads (producers)
    public void addRecordToQueue(StudentRecord record)
            throws InterruptedException {

        // lock the list bc a reader is modifying it
        // or wait until list is unlocked if the mutex is already in use
        mutex.acquire();

        Node newNode = new Node(record);

        // if the tail is empty => there is no head either
        // bc all records have been processed
        if (tail == null) {
            head = newNode;
            tail = newNode;
        }
        // else add to the tail of the queue
        else {
            tail.next = newNode;
            tail = newNode;
        }

        // list has finished being modified
        mutex.release();

        // an item has been added => increase items semaphore
        items.release();
    }

    // Called by worker threads (consumers)
    public StudentRecord dequeueRecord()
            throws InterruptedException {

        // decrease the semaphore bc the worker is currently processing
        // one of the records so it took it off of the queue
        items.acquire();

        // lock the queue so no other worker can accidentally end up removing
        // the same item at the same time
        mutex.acquire();

        StudentRecord record = head.record;

        head = head.next;

        if (head == null) {
            tail = null;
        }

        mutex.release();

        return record;
    }
}
