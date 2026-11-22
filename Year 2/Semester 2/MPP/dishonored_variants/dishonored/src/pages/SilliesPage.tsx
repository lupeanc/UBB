import ImagePreview from "../components/ImagePreview";
import "./SilliesPage.css";

const SilliesPage = () => {
  return (
    <>
      <div className="main-div-sillies-page">
        <div className="sillies-page-container">
          <h2 className="title-sillies">SILLIES</h2>
          <div className="sillies-container">
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
      </div>
    </>
  );
};

export default SilliesPage;
