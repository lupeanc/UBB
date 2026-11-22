import { useState, useEffect } from "react";
import CharacterIndexTable from "../components/CharacterIndexTable";
import CharacterCard from "../components/CharacterCard";
import "../assets/hero.png";
import NewestPage from "../components/NewestPage";
import NewestSilliesSketch from "../components/NewestSilliesSketch";
// import heroImg from "../assets/hero.png"

export type CharacterType = {
  name: string;
  nickname: string;
  age: number;
  job: string;
  image: string;
};

const MainPage = () => {
  const [characters, setCharacters] = useState<CharacterType[]>([]);

  // Initialize characters once on mount
  useEffect(() => {
    setCharacters([
      {
        name: "Alexander Ward",
        nickname: "-",
        age: 28,
        job: "Prince",
        image: "../public/princeref.png",
      },
      {
        name: "Clayton Wolfe",
        nickname: "-",
        age: 28,
        job: "Knight",
        image: "../public/knightref.png",
      },
    ]);
  }, []); // empty dependency array → runs only once

  return (
    <>
      <h2>--HOME PAGE--</h2>
      <NewestPage />
      <div className="silly-sketch-div">
        <NewestSilliesSketch divType={"silly"} />
        <NewestSilliesSketch divType={"sketch"} />
      </div>

      <br></br>
      <br></br>
      <br></br>
      <h2>--CHARACTER INDEX--</h2>
      <CharacterIndexTable
        characters={characters}
        setCharacters={setCharacters}
      />
      <div className="character-cards-container">
        {characters.map((character, index) => (
          <CharacterCard key={index} character={character} />
        ))}
      </div>
    </>
  );
};

export default MainPage;
