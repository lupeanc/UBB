import ImagePreview from "./ImagePreview";
import "./ChapterComponent.css";
import { useState } from "react";
import { motion } from "motion/react";

// add on click show this stuff using states
const ChapterComponent = () => {
  const [isVisible, setIsVisible] = useState(false);
  return (
    <>
      <div className="main-div-chapter-component">
        <div className="chapter-title-div">
          <motion.h2
            className="title-chapter"
            onClick={() => {
              setIsVisible(!isVisible);
            }}
            whileHover={{ scale: 1.01 }}
            whileTap={{ scale: 1 }}
          >
            CHAPTER 1
          </motion.h2>
        </div>

        <hr color=""></hr>
        {isVisible ? (
          <motion.div
            className="chapters-container"
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.3 }}
          >
            <ImagePreview />
            <ImagePreview />
            <ImagePreview />
            <ImagePreview />
            <ImagePreview />
            <ImagePreview />
            <ImagePreview />
            <ImagePreview />
            <ImagePreview />
          </motion.div>
        ) : (
          <div></div>
        )}
      </div>
    </>
  );
};

export default ChapterComponent;
