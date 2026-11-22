// import heroImg from "../assets/hero.png";
import "./NewestPage.css";

const NewestPage = () => {
  return (
    <>
      <div className="main-div">
        <h2 className="title">NEWEST PAGE</h2>
        <hr color="grey"></hr>
        <div className="flex-container">
          <div className="image-container">
            <img src="../public/2.png" alt="" className="image-fit"></img>
          </div>

          {/* <div className="clear"></div> */}
          <div className="description">
            NEWEST PAGE OUT NOW! Modern AU - New addition, incredible, and quite
            never heard of, am i right? Anywho, enjoy the dive into a new
            parallel universe, where the events are set in the modern world,
            rather than the medival ages :) (spoiler alert, the main characters
            are still assholes)
            <br></br>
            <br></br>
            Also - text lyrics are from "Slow dance" by Artemas!
          </div>
        </div>
      </div>
    </>
  );
};

export default NewestPage;
