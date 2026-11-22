import NewestPage from "../components/NewestPage";
import NewestSilliesSketch from "../components/NewestSilliesSketch";

const HomePage = () => {
  return (
    <>
      <NewestPage />

      <div className="silly-sketch-div">
        <NewestSilliesSketch divType={"silly"} />
        <NewestSilliesSketch divType={"sketch"} />
      </div>
    </>
  );
};

export default HomePage;
