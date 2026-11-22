import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import "./style.css";

const HomePage = () => {
  const location = useLocation();
  const user = location.state?.user;
  const [courses, setCourses] = useState<any[]>([]);
  const [students, setStudents] = useState<any[]>([]);
  const [studentsToCourse, setStudentsToCourse] = useState<any[]>([]);
  const [studentCourses, setStudentCourses] = useState<any[]>([]);
  const [selectedCourse, setSelectedCourse] = useState("");
  const [selectedStudent, setSelectedStudent] = useState("");
  const [grade, setGrade] = useState("");
  const [courseGrade, setCourseGrade] = useState("");

  //ISO DATE FORMAT!!!
  // const [date, setDate] = useState(new Date().toISOString().split("T")[0]);

  useEffect(() => {
    fetch(`http://localhost:8000/controller/Controller.php?action=getCourses`)
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setCourses(result);
      });

    fetch(`http://localhost:8000/controller/Controller.php?action=getStudents`)
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setStudents(result);
      });
  }, []);

  const getStudentsToCourse = (course: string) => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getStudentsToCourse&coursename=${course}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setStudentsToCourse(result);
      });
  };

  const getStudentCourses = (student: string) => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getStudentCourses&name=${student}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setStudentCourses(result);
      });
  };

  const addStudentGrade = () => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=addStudentGrade&professorid=${user.id}&name=${selectedStudent}&coursename=${courseGrade}&grade=${grade}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        window.location.reload();
      });
  };

  return (
    <>
      <h1>HOME</h1>
      <select
        value={selectedCourse}
        onChange={(e) => {
          // e.preventDefault();
          setSelectedCourse(e.target.value);
          getStudentsToCourse(e.target.value);
        }}
      >
        {courses.map((c) => (
          <>
            <option value={c.coursename}>{c.coursename}</option>
          </>
        ))}
      </select>
      <div>
        {studentsToCourse.map((student) => (
          <div>{student.participants}</div>
        ))}
      </div>

      <select
        value={selectedStudent}
        onChange={(e) => {
          setSelectedStudent(e.target.value);
          getStudentCourses(e.target.value);
        }}
      >
        {students.map((s) => (
          <option value={s.name}>{s.name}</option>
        ))}
      </select>

      <table>
        <tr>
          <th>ID</th>
          <th>Course Name</th>
          <th>Professor Name</th>
          <th>Participants</th>
          <th>Grades</th>
        </tr>
        {studentCourses.map((c) => (
          <>
            <tr>
              <th>{c.id}</th>
              <th>{c.professorid}</th>
              <th>{c.coursename}</th>
              <th>{c.participants}</th>
              <th>{c.grades}</th>
            </tr>
          </>
        ))}
      </table>

      <form
        onSubmit={(e) => {
          e.preventDefault();
        }}
      >
        <label>Grade for selected student:</label>
        <input value={grade} onChange={(e) => setGrade(e.target.value)}></input>
        <label>Course:</label>
        <input
          value={courseGrade}
          onChange={(e) => setCourseGrade(e.target.value)}
        ></input>
        <button type="submit" onClick={() => addStudentGrade()}>
          Add
        </button>
      </form>
    </>
  );
};

export default HomePage;
