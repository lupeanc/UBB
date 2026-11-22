import { Link } from "react-router-dom";
import CharacterCard from "../components/CharacterCard";
import "./CharacterIndexPage.css";

export type CharacterType = {
  name: string;
  nickname: string;
  age: number;
  job: string;
  image: string;
};

const CharacterIndexPage = ({ isAdmin, characterList }) => {
  // const characters: Array<CharacterType> = [
  //   {
  //     name: "Knightu ba",
  //     nickname: "Knightu ba",
  //     age: 28,
  //     job: "..knight gen",
  //     image: "../assets/hero.png",
  //   },
  //   {
  //     name: "Knightu ba",
  //     nickname: "Knightu ba",
  //     age: 28,
  //     job: "..knight gen",
  //     image: "../assets/hero.png",
  //   },
  //   {
  //     name: "Knightu ba",
  //     nickname: "Knightu ba",
  //     age: 28,
  //     job: "..knight gen",
  //     image: "../assets/hero.png",
  //   },
  //   {
  //     name: "Knightu ba",
  //     nickname: "Knightu ba",
  //     age: 28,
  //     job: "..knight gen",
  //     image: "../assets/hero.png",
  //   },
  // ];

  const characters = characterList;

  return (
    <>
      <div className="main-div-character-index ">
        <div className="edit-div">
          {isAdmin ? (
            <Link
              to="/character-index-table"
              className="edit-button-character-index-admin"
            >
              Edit
            </Link>
          ) : (
            <></>
          )}
        </div>
        <div className="characters-container">
          {characters.map((character) => (
            <CharacterCard character={character} />
          ))}
        </div>
      </div>
    </>
  );
};
export default CharacterIndexPage;
