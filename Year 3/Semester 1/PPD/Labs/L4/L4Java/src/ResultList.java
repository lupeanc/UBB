import java.io.BufferedWriter;
import java.io.IOException;

public class ResultList {

    private static class Node {
        int id;
        int grade;
        Node next;

        Node(int id, int grade) {
            this.id = id;
            this.grade = grade;
            this.next = null;
        }
    }

    private Node head;

    public ResultList() {
        head = null;
    }

    public synchronized void addOrUpdate(int id, int grade) {

        // Case 1: The list is empty.
        if (head == null) {
            head = new Node(id, grade);
            return;
        }

        // Case 2: The new ID is smaller than the first ID.
        if (id < head.id) {
            Node newNode = new Node(id, grade);
            newNode.next = head;
            head = newNode;
            return;
        }

        Node current = head;

        // Find the correct position.
        // Go through the list until the next id is bigger or equal
        // => thats our position
        while (current.next != null && current.next.id < id) {
            current = current.next;
        }

        // Case 3: The ID already exists.
        // We found the next position, so we check if it is equal
        // if yes => update current node
        // special equal for the head
        if (current.id == id) {
            current.grade += grade;
        }
        // if its not the head, it will be the next term in line
        else if (current.next != null && current.next.id == id) {
            current.next.grade += grade;
        }
        // Case 4: Insert a new node.
        else {
            Node newNode = new Node(id, grade);
            newNode.next = current.next;
            current.next = newNode;
        }
    }

    public synchronized void writeToFile(BufferedWriter writer)
            throws IOException {

        Node current = head;

        while (current != null) {
            writer.write(current.id + "," + current.grade);
            writer.newLine();

            current = current.next;
        }
    }

    public synchronized boolean equals(ResultList resultList) {
        if (resultList == null) {
            return false;
        }

        Node currentThisList = head;
        Node currentOtherList = resultList.head;

        while(currentThisList != null  && currentOtherList != null) {
            if (currentThisList.id != currentOtherList.id ||
            currentThisList.grade != currentOtherList.grade) {
                return false;
            }
            currentThisList = currentThisList.next;
            currentOtherList = currentOtherList.next;
        }

        return currentThisList == null && currentOtherList == null;
    }
}
