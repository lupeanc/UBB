
public class StudentRecord {
    private int id;
    private int grade;
    private boolean allRecordsHaveBeenRead;

    // one of the student records
    public StudentRecord(int id, int grade) {
        this.id = id;
        this.grade = grade;
        this.allRecordsHaveBeenRead = false;
    }

    private StudentRecord() {
        this.allRecordsHaveBeenRead = true;
    }

    // create a final record to tell the worker threads
    // that their work is done
    // (the reader threads have finished reading their section)
    public static StudentRecord createFinalRecord() {
        return new StudentRecord();
    }

    public int getId() {
        return id;
    }

    public int getGrade() {
        return grade;
    }

    public boolean checkAllRecordsHaveBeenRead() {
        return allRecordsHaveBeenRead;
    }
}
