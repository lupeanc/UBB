import { Link } from "react-router-dom";
import CharacterIndexTable from "../components/CharacterIndexTable";
import "./CharacterIndexTablePage.css";

const CharacterIndexTablePage = () => {
  return (
    <>
      <div className="main-div-character-index-table-page">
        <div className="save-character-index-table-div">
          <Link to="/character-index" className="save-character-index-table">
            Save and Go Back
          </Link>
        </div>

        <div>
          <CharacterIndexTable />
        </div>
      </div>
    </>
  );
};

export default CharacterIndexTablePage;
