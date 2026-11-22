import { Link } from "react-router-dom";
import UserProfileInfo from "../components/UserProfileInfo";
import "./UserProfilePage.css";
import { SlCheck, SlFolder, SlFolderAlt, SlPencil } from "react-icons/sl";
import { useState } from "react";
import UserProfileEdit from "../components/UserProfileEdit";

// const [username, setUsername] = useState("");
// const [description, setDescription] = useState("");

const UserProfilePage = ({ username, description, pfpImg }) => {
  const [isEditing, setIsEditing] = useState(false);
  // const [username, setUsername] = useState("");
  // const [description, setDescription] = useState("");
  // const [pfpImg, setPfpImg] = useState("");

  // setUsername("claylex-shipper");
  // setDescription("deeeeesc");
  // setPfpImg("../public/knightref.png");

  return (
    <>
      <div className="main-div-user-profile-page">
        {isEditing ? (
          <div className="main-div-user-profile-page">
            <UserProfileEdit />
            <button
              type="button"
              className="save-profile"
              onClick={() => {
                setIsEditing(!isEditing);
              }}
            >
              <SlFolderAlt />
            </button>
          </div>
        ) : (
          <div className="main-div-user-profile-page">
            <UserProfileInfo
              username={username}
              description={description}
              pfpImg={pfpImg}
            />
            <button
              type="button"
              className="edit-profile"
              onClick={() => {
                setIsEditing(!isEditing);
              }}
            >
              <SlPencil />
            </button>
          </div>
        )}
      </div>
    </>
  );
};

export default UserProfilePage;
