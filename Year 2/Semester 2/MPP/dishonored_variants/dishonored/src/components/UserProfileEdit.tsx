// import { Link } from "react-router-dom";
import { useState } from "react";
import heroImg from "../assets/hero.png";
import "./UserProfileEdit.css";
// const saveChanges = (e) => {};

const UserProfileEdit = () => {
  const [username, setUsername] = useState("");
  const [profileImg, setProfileImg] = useState("");
  const [description, setDescription] = useState("");

  const saveChanges = (e) => {
    e.preventDefault();
    setUsername(username);
    setProfileImg(profileImg);
    setDescription(description);
  };

  return (
    <>
      <div className="main-div-user-edit">
        <div className="user-info-container">
          <div className="pfp-container">
            <img src={heroImg} className="pfp"></img>
          </div>

          <form onSubmit={saveChanges}>
            <input
              type="text"
              placeholder="Username"
              className="form-field-user-edit"
              value={username}
              onChange={(e) => {
                setUsername(e.target.value);
              }}
            ></input>
            <span
              className="user-edit-description"
              role="textbox"
              contentEditable
            ></span>
            {/* <input
            type="description"
            placeholder="Description"
            className="form-field-user-edit-large"
            value={description}
            onChange={(e) => {
              setDescription(e.target.value);
            }}
          ></input> */}
          </form>
        </div>

        <div className="account-info-div">
          <div className="account-info-title">ACCOUNT INFORMATION</div>
          <form>
            <label className="account-info-input-label" htmlFor="email">
              Email:
            </label>
            <input
              id="email"
              type="text"
              // placeholder="Email"
              className="form-field-user-edit-account-info"
            ></input>
            <br></br>
            <label className="account-info-input-label" htmlFor="password">
              Password:
            </label>
            <input
              id="password"
              type="text"
              // placeholder="Password"
              className="form-field-user-edit-account-info"
            ></input>
          </form>
        </div>
      </div>
    </>
  );
};

export default UserProfileEdit;
