import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import type { Step } from "./stepBuilderpage";

const ReviewPage = () => {
  const location = useLocation();
  const user = location.state?.user;
  const title = location.state?.title;
  const steps = location.state?.steps;
  const navigate = useNavigate();

  const goBack = () => {
    navigate("/stepBuilder", {
      state: { user: user, title: title, steps: steps },
    });
  };

  const addRecipe = () => {};

  return (
    <>
      <table>
        <tr>
          <th>Description</th>
          <th>Ingredients</th>
        </tr>
        {steps.map((s: Step) => (
          <>
            <tr>
              <th>{s.description}</th>
              <th>{s.ingredients}</th>
            </tr>
          </>
        ))}
      </table>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          addRecipe();
          // goNext();
        }}
      >
        <label>Review:</label>
        {/* <input value={title} onChange={(e) => setTitle(e.target.value)}></input> */}
        <button type="submit">Done</button>
      </form>
      <button type="submit" onClick={(e) => goBack()}></button>
    </>
  );
};
export default ReviewPage;
