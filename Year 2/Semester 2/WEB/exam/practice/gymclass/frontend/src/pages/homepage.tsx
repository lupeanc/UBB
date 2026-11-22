import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import "./styles.css";

const HomePage = () => {
  const location = useLocation();
  const user = location.state?.user;
  const [classes, setClasses] = useState<any[]>([]);

  // const [className, setClassName] = useState("");

  const [id, setId] = useState("");
  // MAKES IT HAVE THE RIGHT FORMAT!!!
  const [bookedAt, setBookedAt] = useState(new Date().toLocaleString("sv-SE"));

  //ISO DATE FORMAT!!!
  // const [date, setDate] = useState(new Date().toISOString().split("T")[0]);

  useEffect(() => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getUserBookingClasses&user=${user.username}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setClasses(result);
      });
  }, []);

  const addBooking = () => {
    if (id && bookedAt) {
      fetch(
        `http://localhost:8000/controller/Controller.php?action=addBooking&userId=${user.id}&classId=${id}&bookedAt=${bookedAt}&cancelled=0`,
      )
        .then((res) => res.json())
        .then((result) => {
          console.log(result);
          if (result.result) {
            alert(result.result);
          } else {
            window.location.reload();
          }
        });
    }
  };

  const cancelBooking = () => {
    if (id) {
      fetch(
        `http://localhost:8000/controller/Controller.php?action=cancelBooking&userId=${user.id}&classId=${id}`,
      )
        .then((res) => res.json())
        .then((result) => {
          console.log(result);
          // alert("class cancelled");
          window.location.reload();
        });
    }
  };

  return (
    <>
      <h1>HOME</h1>
      <br></br>
      <table>
        <thead>
          <tr>
            <th>Class ID</th>
            <th>Class Name</th>
            <th>Instructor Name</th>
            <th>Date</th>
            <th>Capacity</th>
          </tr>
        </thead>
        <tbody>
          {classes.map((c) => (
            <>
              <tr>
                <td>{c.id}</td>
                <td>{c.className}</td>
                <td>{c.instructorName}</td>
                <td>{c.classDate}</td>
                <td>{c.maxCapacity}</td>
              </tr>
            </>
          ))}
        </tbody>
      </table>

      <br></br>
      <form onSubmit={(e) => e.preventDefault()}>
        <label>ClassID:</label>
        <input value={id} onChange={(e) => setId(e.target.value)}></input>
        <label>Booked At</label>
        <input
          value={bookedAt}
          onChange={(e) => setBookedAt(e.target.value)}
        ></input>
      </form>
      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          addBooking();
        }}
      >
        Book a Class
      </button>

      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          cancelBooking();
        }}
      >
        Cancel a Class
      </button>
    </>
  );
};

export default HomePage;

// const HomePage = () => {
//   return <h1>home</h1>;
// };
// export default HomePage;
