// import heroImg from "../assets/hero.png";
import "./CharacterCard.css";

const CharacterCard = ({ character }) => {
  return (
    <>
      <div className="character-card-div">
        <div className="flex-container-character-card">
          <div className="image-container-character-card">
            <img
              src={character.image}
              alt=""
              className="image-fit-character-card"
            ></img>
          </div>

          {/* <div className="clear"></div> */}
          <div className="attribute-container">
            <div className="attribute">
              <b>Name: </b>
              {character.name}
            </div>
            <div className="attribute">
              <b>Nickname: </b>
              {character.nickname}
            </div>
            <div className="attribute">
              <b>Age: </b>
              {character.age}
            </div>
            <div className="attribute">
              <b>Job: </b>
              {character.job}
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default CharacterCard;
