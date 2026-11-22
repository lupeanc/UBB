import "./CharacterIndexTable.css";
import React, { useState } from "react";
// import validator from "validator";

export type CharacterType = {
  name: string;
  nickname: string;
  age: number;
  job: string;
  image: string;
};

const CharacterIndexTable = () => {
  const characters: Array<CharacterType> = [
    {
      name: "Knightu ba",
      nickname: "Knightu ba",
      age: 28,
      job: "..knight gen",
      image: "../assets/hero.png",
    },
  ];

  const [data, setData] = useState<CharacterType[]>(characters);
  const [error, setError] = useState<string>("");
  const [editIndex, setEditIndex] = useState<number | null>(null);

  const [name, setName] = useState("");
  const [nickname, setNickname] = useState("");
  const [age, setAge] = useState("");
  const [job, setJob] = useState("");
  const [image, setImage] = useState("");

  const handleAdd = (e: React.FormEvent) => {
    e.preventDefault();

    if (Number(age) <= 0 || Number(age) > 100) {
      setError("Age must be greater than 0, and smaller than 100 (cmon bro.)");
      return;
    }

    setError("");

    const newCharacter: CharacterType = {
      name,
      nickname,
      age: Number(age),
      job,
      image,
    };

    // if in edit mode: ... if not => add
    // this way i can also check the inputs from the edits.
    if (editIndex !== null) {
      const updated = [...data];
      updated[editIndex] = newCharacter;
      setData(updated);
      setEditIndex(null);
    } else {
      setData([...data, newCharacter]);
    }

    // clear form
    setName("");
    setNickname("");
    setAge("");
    setJob("");
    setImage("");
  };

  const handleRemove = (index: number) => {
    const updated = data.filter((_, i) => i !== index);
    setData(updated);
  };

  const handleEdit = (index: number) => {
    const character = data[index];

    setName(character.name);
    setNickname(character.nickname);
    setAge(String(character.age));
    setJob(character.job);
    setImage(character.image);

    setEditIndex(index);
  };

  return (
    <>
      {/* if error has value, show */}
      <div className="character-index-table-container">
        {error && <p style={{ color: "red", fontSize: "15px" }}>{error}</p>}
        <div className="form-div">
          <form onSubmit={handleAdd}>
            <input
              type="text"
              placeholder="Enter Name"
              className="form-field"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />

            <input
              type="text"
              placeholder="Enter Nickname"
              className="form-field"
              value={nickname}
              onChange={(e) => setNickname(e.target.value)}
            />

            <input
              type="number"
              placeholder="Enter Age"
              className="form-field"
              value={age}
              onChange={(e) => setAge(e.target.value)}
            />

            <input
              type="text"
              placeholder="Enter Job"
              className="form-field"
              value={job}
              onChange={(e) => setJob(e.target.value)}
            />

            <input
              type="text"
              placeholder="Enter Image Path"
              className="form-field"
              value={image}
              onChange={(e) => setImage(e.target.value)}
            />
            <button
              type="submit"
              className="action-button"
              disabled={!name || !age || !job || !image}
            >
              Add
            </button>
          </form>
        </div>

        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Nickname</th>
              <th>Age</th>
              <th>Job</th>
              <th>Image Link</th>
              <th>Action</th>
            </tr>
          </thead>

          <tbody>
            {data.map((character, index) => (
              <tr key={index}>
                <td>{character.name}</td>
                <td>{character.nickname}</td>
                <td>{character.age}</td>
                <td>{character.job}</td>
                <td>{character.image}</td>
                <td>
                  <button
                    className="action-button"
                    onClick={() => handleEdit(index)}
                  >
                    Edit
                  </button>

                  <button
                    className="action-button"
                    onClick={() => handleRemove(index)}
                  >
                    Remove
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
};

export default CharacterIndexTable;
