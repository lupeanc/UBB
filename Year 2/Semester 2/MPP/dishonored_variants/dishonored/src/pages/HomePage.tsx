import NewestPage from "../components/NewestPage";
import NewestSilliesSketch from "../components/NewestSilliesSketch";
import "./HomePage.css";

const HomePage = () => {
  return (
    <>
      <div className="main-div-home-page">
        <div className="home-page-container">
          <NewestPage />

          <div className="silly-sketch-div">
            <NewestSilliesSketch divType={"silly"} />
            <NewestSilliesSketch divType={"sketch"} />
          </div>
        </div>
      </div>
    </>
  );
};

export default HomePage;
