import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import "./styles.css";

const HomePage = () => {
  const location = useLocation();
  const user = location.state?.user;
  const [classes, setClasses] = useState<any[]>([]);
  const [classId, setClassId] = useState("");
  const [bookedAt, setBookedAt] = useState(new Date().toLocaleString("sv-SE"));
  const [allClasses, setAllClasses] = useState<any[]>([]);
  const [selectedBooking, setSelectedBooking] = useState("");

  useEffect(() => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getUserClasses&user=${user.username}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log("USER CLASSES:");
        console.log(result);
        setClasses(result);
      });

    fetch(`http://localhost:8000/controller/Controller.php?action=getClasses`)
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setAllClasses(result);
      });
  }, []);

  const addBooking = () => {
    if (classId) {
      fetch(
        `http://localhost:8000/controller/Controller.php?action=addBooking&user=${user.id}&classId=${classId}&bookedAt=${bookedAt}`,
      )
        .then((res) => res.json())
        .then((result) => {
          console.log(result);
          if (result && result.result) {
            if (result.result == "basic") {
              alert("High intensity - pay us more");
            } else if (result.result == "maxCapacity") {
              allClasses.forEach((c) => {
                if (c.id == classId) {
                  alert(
                    `You've been added to the waitlist for class ${c.className}!`,
                  );
                }
              });
            }
          } else {
            alert("added booking!");
          }
        });

      window.location.reload();
    }
  };

  const cancelBooking = () => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=cancelBooking&user=${user.id}&classId=${selectedBooking}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log("GOT THIS:");
        console.log(result);
        if (result && result.result != "null") {
          alert(
            `${result.result} has been removed from waitlist and booked a class in ur place! Loser`,
          );
        }
      });
    // window.location.reload();
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
        <label>Class ID</label>
        <input value={classId} onChange={(e) => setClassId(e.target.value)} />
        <label>Date</label>
        <input value={bookedAt} onChange={(e) => setBookedAt(e.target.value)} />
      </form>

      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          addBooking();
          // window.location.reload();
        }}
      >
        Book a Class
      </button>

      <br></br>

      <select
        value={selectedBooking}
        onChange={(e) => setSelectedBooking(e.target.value)}
      >
        <option>Choose Booking</option>
        {classes.map((c) => (
          <option value={c.id}>
            {c.id} - {c.className}: {c.classDate}
          </option>
        ))}
      </select>

      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          cancelBooking();
        }}
      >
        Cancel Booking
      </button>
    </>
  );
};

export default HomePage;
