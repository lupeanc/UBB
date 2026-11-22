import { useState } from "react";
import { useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const TitlePage = () => {
  const location = useLocation();
  const user = location.state?.user;
  const navigate = useNavigate();
  const [title, setTitle] = useState("");
  const [steps, setSteps] = useState<any[]>([]);

  const goNext = () => {
    navigate("/stepBuilder", {
      state: { user: user, title: title, steps: steps },
    });
  };

  return (
    <>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          goNext();
        }}
      >
        <label>Title:</label>
        <input value={title} onChange={(e) => setTitle(e.target.value)}></input>
        <button type="submit">Next</button>
      </form>
    </>
  );
};
export default TitlePage;
