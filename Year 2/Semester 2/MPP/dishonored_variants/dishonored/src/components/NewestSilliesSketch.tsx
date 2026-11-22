import heroImg from "../assets/hero.png";
import "./NewestSilliesSketch.css";

const NewestSilliesSketch = ({ divType }) => {
  let mainDivClass = "";
  if (divType == "silly") {
    mainDivClass = "main-div-left";
  } else if ((divType = "sketch")) {
    mainDivClass = "main-div-right";
  }
  return (
    <>
      <div className={mainDivClass}>
        <h3 className="title-ss">NEWEST {divType.toUpperCase()}</h3>

        <img src={heroImg} alt="" className="image-fit-ss"></img>

        <div className="description-ss">
          Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque
          faucibus ex sapien vitae pell
        </div>
      </div>
    </>
  );
};

export default NewestSilliesSketch;
