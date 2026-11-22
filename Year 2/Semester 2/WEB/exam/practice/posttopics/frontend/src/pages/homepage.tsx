import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import "./styles.css";

const HomePage = () => {
  const location = useLocation();
  const user = location.state?.user;
  const [posts, setPosts] = useState<any[]>([]);
  // MAKES IT HAVE THE RIGHT FORMAT!!!
  const [date, setDate] = useState(new Date().toLocaleString("sv-SE"));
  const [id, setId] = useState("");
  const [topicid, setTopicId] = useState("");
  const [postuser, setPostUser] = useState("");
  const [text, setText] = useState("");
  const [postdate, setPostDate] = useState("");
  const [topicname, setTopicName] = useState("");

  //ISO DATE FORMAT!!!
  // const [date, setDate] = useState(new Date().toISOString().split("T")[0]);

  useEffect(() => {
    fetch(`http://localhost:8000/controller/Controller.php?action=getPosts`)
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setPosts(result);
      });
  }, []);

  const setData = (
    id: string,
    postuser: string,
    topicid: string,
    text: string,
    date: string,
  ) => {
    setId(id);
    setPostUser(postuser);
    setTopicId(topicid);
    setText(text);
    setPostDate(date);
  };

  const setAddData = () => {
    setPostUser(user.user);
    setPostDate(date);
  };

  const updatePost = () => {
    if (id && postuser && topicid && text && postdate)
      fetch(
        `http://localhost:8000/controller/Controller.php?action=updatePost&id=${id}&user=${postuser}&topicid=${topicid}&text=${text}&date=${date}`,
      )
        .then((res) => res.json())
        .then((result) => {
          console.log(result);
          window.location.reload();
        });
  };

  const addPost = () => {
    if (postuser && topicname && text && postdate)
      fetch(
        `http://localhost:8000/controller/Controller.php?action=addPost&user=${postuser}&topicname=${topicname}&text=${text}&date=${date}`,
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
      <br></br>
      <table>
        <tr>
          <th>Post ID</th>
          <th>User</th>
          <th>Topic ID</th>
          <th>Text</th>
          <th>Date</th>
        </tr>
        {posts.map((p) => (
          <>
            <tr>
              <th>{p.id}</th>
              <th>{p.user}</th>
              <th>{p.topicid}</th>
              <th>{p.text}</th>
              <th>{p.date}</th>
              <th>
                <button
                  type="submit"
                  onClick={(e) => {
                    e.preventDefault();
                    setData(p.id, p.user, p.topicid, p.text, p.date);
                  }}
                >
                  Fetch
                </button>
              </th>
            </tr>
          </>
        ))}
      </table>
      <br></br>
      <form onSubmit={(e) => e.preventDefault()}>
        <label>Post ID:</label>
        <input value={id} readOnly></input>
        <label>User:</label>
        <input
          value={postuser}
          onChange={(e) => setPostUser(e.target.value)}
        ></input>
        <label>Topic ID:</label>
        <input
          value={topicid}
          onChange={(e) => setTopicId(e.target.value)}
        ></input>
        <label>Text:</label>
        <input value={text} onChange={(e) => setText(e.target.value)}></input>
        <label>Date:</label>
        <input
          value={postdate}
          onChange={(e) => setPostDate(e.target.value)}
        ></input>
        <label>Topic Name:</label>
        <input
          value={topicname}
          onChange={(e) => setTopicName(e.target.value)}
        ></input>
      </form>

      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          updatePost();
        }}
      >
        Update
      </button>

      <br></br>
      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          setAddData();
        }}
      >
        Fetch for Add
      </button>
      <br></br>
      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          addPost();
        }}
      >
        Add Post
      </button>
    </>
  );
};

export default HomePage;

// const HomePage = () => {
//   return <h1>home</h1>;
// };
// export default HomePage;
