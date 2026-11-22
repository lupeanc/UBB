import React, { useState } from "react";
import type { CharacterType } from "../pages/MainPage";
import "./CharacterIndexTable.css";

const isValidImage = (url: string): Promise<boolean> => {
  return new Promise((resolve) => {
    const img = new Image();
    img.src = url;

    img.onload = () => resolve(true);
    img.onerror = () => resolve(false);
  });
};

type Props = {
  characters: CharacterType[];
  setCharacters: React.Dispatch<React.SetStateAction<CharacterType[]>>;
};

const CharacterIndexTable: React.FC<Props> = ({
  characters,
  setCharacters,
}) => {
  const [editIndex, setEditIndex] = useState<number | null>(null);
  const [name, setName] = useState("");
  const [nickname, setNickname] = useState("");
  const [age, setAge] = useState("");
  const [job, setJob] = useState("");
  const [image, setImage] = useState("");
  const [error, setError] = useState("");

  async function handleAdd(e: React.FormEvent) {
    e.preventDefault();

    if (!name || !nickname || !age || !job || !image) {
      setError("All fields are required");
      return;
    }

    if (Number(age) <= 0) {
      setError("Age must be greater than 0");
      return;
    }
    const validImage = await isValidImage(image);

    if (!validImage) {
      setError("Image path is invalid or cannot be loaded");
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

    if (editIndex !== null) {
      const updated = [...characters];
      updated[editIndex] = newCharacter;
      setCharacters(updated);
      setEditIndex(null);
    } else {
      setCharacters([...characters, newCharacter]);
    }

    setName("");
    setNickname("");
    setAge("");
    setJob("");
    setImage("");
  }

  const handleEdit = (index: number) => {
    const char = characters[index];
    setName(char.name);
    setNickname(char.nickname);
    setAge(String(char.age));
    setJob(char.job);
    setImage(char.image);
    setEditIndex(index);
  };

  const handleRemove = (index: number) => {
    setCharacters(characters.filter((_, i) => i !== index));
    if (editIndex === index) setEditIndex(null);
  };

  return (
    <div>
      <div className="form-div">
        {error && <p style={{ color: "red", fontSize: "15px" }}>{error}</p>}
        <form onSubmit={handleAdd}>
          <input
            id="Name"
            className="form-field"
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <input
            className="form-field"
            placeholder="Nickname"
            value={nickname}
            onChange={(e) => setNickname(e.target.value)}
          />
          <input
            className="form-field"
            placeholder="Age"
            type="number"
            value={age}
            onChange={(e) => setAge(e.target.value)}
          />
          <input
            className="form-field"
            placeholder="Job"
            value={job}
            onChange={(e) => setJob(e.target.value)}
          />
          <input
            className="form-field"
            placeholder="Image"
            value={image}
            onChange={(e) => setImage(e.target.value)}
          />
          <button
            type="submit"
            className="action-button"
            // disabled={!name || !age || !job || !image}
          >
            {editIndex !== null ? "Update" : "Add"}
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
            <th>Image</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {characters.map((char, index) => (
            <tr key={index}>
              <td>{char.name}</td>
              <td>{char.nickname}</td>
              <td>{char.age}</td>
              <td>{char.job}</td>
              <td>{char.image}</td>
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
  );
};

export default CharacterIndexTable;
