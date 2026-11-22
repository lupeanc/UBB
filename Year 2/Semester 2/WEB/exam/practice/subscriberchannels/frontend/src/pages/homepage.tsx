import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import "./styles.css";

const HomePage = () => {
  const location = useLocation();
  const user = location.state?.user;
  const [channelsOwned, setChannelsOwned] = useState<any[]>([]);
  const [channelsSubscribed, setChannelsSubscribed] = useState<any[]>([]);
  const [channelName, setChannelName] = useState("");

  // const [className, setClassName] = useState("");

  // const [id, setId] = useState("");
  // MAKES IT HAVE THE RIGHT FORMAT!!!
  // const [bookedAt, setBookedAt] = useState(new Date().toLocaleString("sv-SE"));

  //ISO DATE FORMAT!!!
  const [date, setDate] = useState(new Date().toISOString().split("T")[0]);

  useEffect(() => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getUserOwnedChannels&user=${user.name}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setChannelsOwned(result);
      });
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getUserSubscribedChannels&user=${user.name}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setChannelsSubscribed(result);
      });
  }, []);

  const subscribe = () => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=subscribeTo&user=${user.name}&channel=${channelName}&date=${date}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        alert(`Subscribed to ${channelName}!`);
        window.location.reload();
      });
  };

  return (
    <>
      <h1>HOME</h1>
      <br></br>
      <table>
        <tr>
          <th>Channel ID</th>
          <th>Owner ID</th>
          <th>Channel Name</th>
          <th>Description</th>
          <th>Subscribers</th>
        </tr>
        {channelsOwned.map((c) => (
          <>
            <tr>
              <th>{c.id}</th>
              <th>{c.ownerid}</th>
              <th>{c.name}</th>
              <th>{c.description}</th>
              <th>{c.subscribers}</th>
            </tr>
          </>
        ))}
      </table>
      <br></br>
      <br></br>
      <h3>SUBBED TO:</h3>
      <table>
        <tr>
          <th>Channel ID</th>
          <th>Owner ID</th>
          <th>Channel Name</th>
          <th>Description</th>
          <th>Subscribers</th>
        </tr>
        {channelsSubscribed.map((c) => (
          <>
            <tr>
              <th>{c.id}</th>
              <th>{c.ownerid}</th>
              <th>{c.name}</th>
              <th>{c.description}</th>
              <th>{c.subscribers}</th>
            </tr>
          </>
        ))}
      </table>
      <br></br>
      <br></br>

      <form onSubmit={(e) => e.preventDefault()}>
        <label>Channel Name:</label>
        <input
          value={channelName}
          onChange={(e) => setChannelName(e.target.value)}
        ></input>
      </form>

      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          subscribe();
        }}
      >
        Subscribe
      </button>
    </>
  );
};

export default HomePage;

// const HomePage = () => {
//   return <h1>home</h1>;
// };
// export default HomePage;
