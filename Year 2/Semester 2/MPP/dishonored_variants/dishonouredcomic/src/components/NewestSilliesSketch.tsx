// import heroImg from "../assets/hero.png";
import "./NewestSilliesSketch.css";

const NewestSilliesSketch = ({ divType }) => {
  let mainDivClass = "";
  let imgSrc = "";
  let desc = "";
  if (divType === "silly") {
    mainDivClass = "main-div-left";
    imgSrc = "../public/adventure-time-fart-noise.jpg";
    desc =
      "That one scary dog privillege (im dyslexic idk how to spell that word) trend - but the knight's short asf";
  } else if (divType === "sketch") {
    mainDivClass = "main-div-right";
    imgSrc = "../public/Prince&Tofu.png";
    desc =
      "Doodle of Modern AU Prince and Tofu :D \n next up maybe i'll actually do smth productive with my time lmao";
  }
  return (
    <>
      <div className={mainDivClass}>
        <h3 className="title-ss">NEWEST {divType.toUpperCase()}</h3>

        <img src={imgSrc} alt="" className="image-fit-ss"></img>

        <div className="description-ss">{desc}</div>
      </div>
    </>
  );
};

export default NewestSilliesSketch;
