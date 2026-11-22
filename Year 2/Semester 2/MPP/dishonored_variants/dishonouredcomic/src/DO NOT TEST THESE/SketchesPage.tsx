import ImagePreview from "../components/ImagePreview";
import "./SketchesPage.css";

const SketchesPage = () => {
  return (
    <>
      <div>
        <h2 className="title-sketches">SKETCHES</h2>
        <div className="sketches-container">
          <div>
            <ImagePreview />
          </div>
          <div>
            <ImagePreview />
          </div>
          <div>
            <ImagePreview />
          </div>
          <div>
            <ImagePreview />
          </div>
          <div>
            <ImagePreview />
          </div>
          <div>
            <ImagePreview />
          </div>
          <div>
            <ImagePreview />
          </div>
          <div>
            <ImagePreview />
          </div>
        </div>
      </div>
    </>
  );
};

export default SketchesPage;
