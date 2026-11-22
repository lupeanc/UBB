import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import "./style.css";

const HomePage = () => {
  const location = useLocation();
  const user = location.state?.user;
  // console.log(user);
  const mapScore = location.state?.mapScore;
  console.log(mapScore);
  const [sessionHistory, setSessionHistory] = useState<any[]>([]);
  const [mapScores, setMapScores] = useState<any[]>(mapScore);
  const [selectedMove, setSelectedMove] = useState(0);
  const [moves, setMoves] = useState<any[]>([]);

  useEffect(() => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getUserSessionHistory&user=${user.username}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setSessionHistory(result);
      });
  }, []);

  const completeMove = () => {
    const copy = [...sessionHistory];

    copy[selectedMove - 1].completed = 1;

    setSessionHistory(copy);

    fetch(`http://localhost:8000/controller/Controller.php?action=getMoves`)
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setMoves(result);

        const score = [...mapScores];

        const moveName = sessionHistory[selectedMove - 1].moveName;
        let muscle: any;

        result.forEach((m: any) => {
          if (m.movename == moveName) {
            muscle = m.muscleGroup;
          }
        });

        score.forEach((s) => {
          if (s.muscleGroup == muscle) {
            s.score += 10;
          }
        });

        setMapScores(score);
      });
  };

  const undoCompleteMove = () => {
    const copy = [...sessionHistory];

    copy[selectedMove - 1].completed = 0;

    setSessionHistory(copy);

    fetch(`http://localhost:8000/controller/Controller.php?action=getMoves`)
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setMoves(result);

        const score = [...mapScores];

        const moveName = sessionHistory[selectedMove - 1].moveName;
        let muscle: any;

        result.forEach((m: any) => {
          if (m.movename == moveName) {
            muscle = m.muscleGroup;
          }
        });

        score.forEach((s) => {
          if (s.muscleGroup == muscle) {
            s.score *= 0.8;
          }
        });

        setMapScores(score);
      });
  };

  return (
    <>
      <h1>HOME</h1>
      <br></br>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>UserId</th>
            <th>MoveId</th>
            <th>MoveName</th>
            <th>Completed</th>
          </tr>
        </thead>

        <tbody>
          {sessionHistory.map((c) => (
            <tr key={c.id}>
              <td>{c.id}</td>
              <td>{c.userid}</td>
              <td>{c.moveid}</td>
              <td>{c.movename}</td>
              <td>{c.completed}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <br></br>
      <h3>SCORES</h3>
      <table>
        <thead>
          <tr>
            <th>MuscleGroup</th>
            <th>Score</th>
          </tr>
        </thead>

        <tbody>
          {mapScores.map((c: any) => (
            <tr key={c.muscleGroup}>
              <td>{c.muscleGroup}</td>
              <td>{c.score}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <select
        value={selectedMove}
        onChange={(e) => setSelectedMove(Number(e.target.value))}
      >
        {sessionHistory.map((s) => (
          <option value={s.id}>
            {s.movename} - {s.id}
          </option>
        ))}
      </select>
      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          completeMove();
        }}
      >
        CompleteMove
      </button>

      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          undoCompleteMove();
        }}
      >
        UndoCompleye
      </button>
    </>
  );
};

export default HomePage;
