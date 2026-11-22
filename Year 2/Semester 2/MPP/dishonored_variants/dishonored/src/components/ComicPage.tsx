import heroImg from "../assets/hero.png";
import "./ComicPage.css";

const ComicPage = () => {
  return (
    <>
      <div className="comic-page-main-div">
        <div className="go-back-comic-page-div">
          <a href="" className="go-back-comic-page">
            Go Back
          </a>
        </div>
        <h3>Chapter 1 - Page 1</h3>
        <img alt="" src={heroImg} className="comic-page"></img>
      </div>
    </>
  );
};

export default ComicPage;
