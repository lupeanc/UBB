import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import "./styles.css";

const HomePage = () => {
  const location = useLocation();
  const user = location.state?.user;
  const [ideas, setIdeas] = useState<any[]>([]);
  const [prevIdeas, setPrevIdeas] = useState<any[]>([]);
  const [comments, setComments] = useState<any[]>([]);
  const [ideaComments, setIdeaComments] = useState<any[]>([]);
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [commentBody, setCommentBody] = useState("");
  const [ideaWithComments, setIdeaWithComments] = useState("");
  const [date, setDate] = useState(new Date().toLocaleString("sv-SE"));
  const [commentDate, setCommentDate] = useState(
    new Date().toLocaleString("sv-SE"),
  );
  const [selectedIdea, setSelectedIdea] = useState("");

  //TIMER
  const [foundIdea, setFoundIdea] = useState(1);
  const [newIdeas, setNewIdeas] = useState<any[]>([]);

  useEffect(() => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getIdeasAndCommentCount`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setIdeas(result);
        if (prevIdeas != result) {
          result.forEach((r: any) => {
            prevIdeas.forEach((i) => {
              if (r == i) {
                setFoundIdea(0);
              }
            });
            if (!foundIdea) {
              setNewIdeas((prev) => [...prev, r]);
              setPrevIdeas(result);
            }
          });
        }
      });

    fetch(`http://localhost:8000/controller/Controller.php?action=getComments`)
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setComments(result);
      });
  }, []);

  const addIdea = () => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=addIdea&user=${user.id}&title=${title}&body=${body}&postedAt=${date}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        // setIdeas(result);
      });
  };

  const addComment = () => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=addComment&user=${user.id}&idea=${selectedIdea}&body=${commentBody}&postedAt=${commentDate}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        // setIdeas(result);
      });
  };

  const addVote = () => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=addVote&user=${user.username}&idea=${selectedIdea}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        // setIdeas(result);
      });
  };

  const getCommentsForIdea = (id: any) => {
    setIdeaComments([]);
    comments.forEach((c) => {
      if (c.ideaId == id) {
        setIdeaComments((prev) => [...prev, c]);
        // ideaComments.push(c);
        console.log(ideaComments);
      }
    });
  };

  return (
    <>
      {/* <meta http-equiv="refresh" content="4"></meta> */}
      <h1>IDEA BOARD</h1>
      <br></br>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Votes</th>
            <th>Number Comments</th>
            <th>Fetch Comments</th>
          </tr>
        </thead>
        <tbody>
          {ideas.map((c) => (
            <>
              <tr>
                <td>{c.idea.title}</td>
                <td>{c.user.username}</td>
                <td>{c.idea.votes}</td>
                <td>{c.commentCount}</td>
                <td>
                  <button
                    type="submit"
                    onClick={(e) => {
                      e.preventDefault();
                      setIdeaWithComments(c.idea.id);
                      getCommentsForIdea(c.idea.id);
                    }}
                  >
                    Fetch Comments
                  </button>
                </td>
              </tr>
            </>
          ))}
        </tbody>
      </table>
      <br></br>
      <h3>COMMENTS FOR IDEA: {ideaWithComments}</h3>
      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          setIdeaComments([]);
          setIdeaWithComments("");
        }}
      >
        Close Comments
      </button>
      <table>
        <thead>
          <tr>
            <th>Author</th>
            <th>Body</th>
            {/* <th>Fetch Comments</th> */}
          </tr>
        </thead>
        <tbody>
          {ideaComments.map((c) => (
            <>
              <tr>
                <td>{c.userId}</td>
                <td>{c.body}</td>
                {/* <td>{c.commentCount}</td> */}
              </tr>
            </>
          ))}
        </tbody>
      </table>

      <br></br>

      <h3>ADD AN IDEA</h3>
      <form onSubmit={(e) => e.preventDefault()}>
        <label>Title:</label>
        <input value={title} onChange={(e) => setTitle(e.target.value)}></input>
        <label>Body:</label>
        <input value={body} onChange={(e) => setBody(e.target.value)}></input>
        <label>Date:</label>
        <input value={date} onChange={(e) => setDate(e.target.value)}></input>
      </form>
      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          addIdea();
        }}
      >
        Add Idea
      </button>
      <br></br>
      <h3>ADD A COMMENT AND VOTE</h3>
      <select
        value={selectedIdea}
        onChange={(e) => setSelectedIdea(e.target.value)}
      >
        <option>CHOOSE</option>
        {ideas.map((c) => (
          <option value={c.idea.id}>
            {c.idea.title}: {c.idea.postedAt}
          </option>
        ))}
      </select>

      <form onSubmit={(e) => e.preventDefault()}>
        <label>Comment Body:</label>
        <input
          value={commentBody}
          onChange={(e) => setCommentBody(e.target.value)}
        ></input>
        <label>Date:</label>
        <input
          value={commentDate}
          onChange={(e) => setCommentDate(e.target.value)}
        ></input>
        <button
          type="submit"
          onClick={(e) => {
            e.preventDefault();
            addComment();
          }}
        >
          Add Comment
        </button>
      </form>

      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          addVote();
        }}
      >
        Vote Idea
      </button>

      <h3>NEW IDEAS</h3>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Votes</th>
            <th>Number Comments</th>
            <th>Fetch Comments</th>
          </tr>
        </thead>
        <tbody>
          {newIdeas.map((c) => (
            <>
              <tr>
                <td>{c.idea.title}</td>
                <td>{c.user.username}</td>
                <td>{c.idea.votes}</td>
                <td>{c.commentCount}</td>
              </tr>
            </>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default HomePage;
