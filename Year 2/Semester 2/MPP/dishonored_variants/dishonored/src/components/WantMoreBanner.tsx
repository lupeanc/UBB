// import { motion } from "motion/react";
import "./WantMoreBanner.css";
import confetti from "canvas-confetti";

const handleClick = (e) => {
  e.preventDefault();
  confetti({
    particleCount: 150,
    spread: 60,
  });
};

const WantMoreBanner = () => {
  return (
    <>
      <div className="banner-main-div">
        <div className="want-more-banner-div">
          <h1 className="want-more-title">WANT MORE?</h1>
          <br></br>
          <a
            href=""
            className="subscribe-button"
            onClick={(e) => handleClick(e)}
          >
            Subscribe to us on Patreon ;)
          </a>
        </div>
      </div>
    </>
  );
};

export default WantMoreBanner;
