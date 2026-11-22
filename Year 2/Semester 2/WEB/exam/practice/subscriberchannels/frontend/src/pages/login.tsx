import { useState } from "react";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {
  const [user, setUser] = useState("");
  const navigate = useNavigate();

  const login = (user: string) => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getUserByUsername&user=${user}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);

        if (result) {
          console.log("User exists");
          // navigate to another page / save user / etc.
          //   const loggedUser = resul/\t[0];
          console.log("Navigating to home...");
          navigate("/home", { state: { user: result } });
        } else {
          console.log("User does not exist");
        }
      });
  };

  return (
    <>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          login(user);
        }}
      >
        <label>User:</label>

        <input value={user} onChange={(e) => setUser(e.target.value)} />

        <button type="submit">LogIn</button>
      </form>
    </>
  );
};

export default LoginPage;
