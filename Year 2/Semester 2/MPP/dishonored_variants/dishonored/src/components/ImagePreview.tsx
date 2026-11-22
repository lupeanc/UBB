import heroImg from "../assets/hero.png";
import "./ImagePreview.css";

const ImagePreview = () => {
  return (
    <>
      <div className="main-div-preview">
        <img src={heroImg} alt="" className="image-fit-preview"></img>
        <h5 className="title-preview">TITLE</h5>
        <h6 className="date">69.69.69</h6>
      </div>
    </>
  );
};

export default ImagePreview;
