import heroImg from "../assets/hero.png";
import "./NewestPage.css";

const NewestPage = () => {
  return (
    <>
      <div className="main-div">
        <h2 className="title">NEWEST PAGE</h2>
        <hr color="#222225"></hr>
        <div className="flex-container">
          <div className="image-container">
            <img src={heroImg} alt="" className="image-fit"></img>
          </div>

          {/* <div className="clear"></div> */}
          <div className="description">
            Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque
            faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi
            pretium tellus duis convallis. Tempus leo eu aenean sed diam urna
            tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas.
            Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut
            hendrerit semper vel class aptent taciti sociosqu. Ad litora
            torquent per conubia nostra inceptos himenaeos.
          </div>
        </div>
      </div>
    </>
  );
};

export default NewestPage;
