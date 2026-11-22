import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import type { Step } from "./stepBuilderPage";

const TitlePage = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const user = location.state?.user;
  const [title, setTitle] = useState("");
  const ingredients: any = [];
  const [steps, setSteps] = useState<Step[]>([]);

  //   useEffect(() => {
  //     fetch(
  //       `http://localhost:8000/controller/Controller.php?action=getIngredients`,
  //     )
  //       .then((res) => res.json())
  //       .then((result) => {
  //         console.log(result);
  //         setIngredients(result);
  //       });
  //   }, []);

  const goNext = () => {
    // console.log(steps);
    if (title) {
      navigate("/stepBuilder", {
        state: { user: user, title: title, steps: steps },
      });
    }
  };

  return (
    <>
      <h2>title</h2>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          goNext();
        }}
      >
        <label>Title:</label>

        <input value={title} onChange={(e) => setTitle(e.target.value)} />

        <button type="submit">Next</button>
      </form>
    </>
  );
};

export default TitlePage;
