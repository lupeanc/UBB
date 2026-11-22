import CharacterCard from "../components/CharacterCard";

export type CharacterType = {
  name: string;
  nickname: string;
  age: number;
  job: string;
  image: string;
};

const CharacterIndexPage = () => {
  const characters: Array<CharacterType> = [
    {
      name: "Knightu ba",
      nickname: "Knightu ba",
      age: 28,
      job: "..knight gen",
      image: "../assets/hero.png",
    },
    {
      name: "Knightu ba",
      nickname: "Knightu ba",
      age: 28,
      job: "..knight gen",
      image: "../assets/hero.png",
    },
    {
      name: "Knightu ba",
      nickname: "Knightu ba",
      age: 28,
      job: "..knight gen",
      image: "../assets/hero.png",
    },
    {
      name: "Knightu ba",
      nickname: "Knightu ba",
      age: 28,
      job: "..knight gen",
      image: "../assets/hero.png",
    },
  ];

  return (
    <>
      {characters.map((character) => (
        <CharacterCard character={character} />
      ))}
    </>
  );
};
export default CharacterIndexPage;
