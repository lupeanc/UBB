import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import type { Step } from "./stepBuilderPage";

const ReviewPage = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const user = location.state?.user;
  const title = location.state?.title;
  const steps = location.state?.steps;
  // const ingredients = location.state?.ingredients;

  const [calories, setCalories] = useState(0);
  const [ingredients, setIngredients] = useState<any[]>([]);

  useEffect(() => {
    let cals = 0;
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getIngredients`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setIngredients(result);

        steps.forEach((step: Step) => {
          // console.log(step);
          step.ingredientList.forEach((i) => {
            console.log("i-" + i);
            result.forEach((ing: any) => {
              console.log("ing-" + ing.name);
              if (ing.name == i) {
                console.log("calories ing " + ing.caloriesPer100g);
                cals += ing.caloriesPer100g;
                console.log("CALS " + cals);
              }
            });
          });
        });

        setCalories(cals);
      });
    // console.log(steps);
  }, []);

  const goNext = () => {
    if (title) {
      navigate("/review", {
        state: {
          user: user,
          title: title,
          steps: steps,
          // ingredients: ingredients,
        },
      });
    }
  };

  const goBack = () => {
    navigate("/stepBuilder", {
      state: {
        user: user,
        title: title,
        steps: steps,
        // ingredients: ingredients,
      },
    });
  };

  const addRecipe = () => {
    console.log(user.username + " " + title + " " + calories);
    fetch(
      `http://localhost:8000/controller/Controller.php?action=addRecipe&user=${user.username}&title=${title}&totalcalories=${calories}`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
      });
  };

  return (
    <>
      <h2>Review</h2>
      <h3>Title: {title}</h3>
      <h3>Steps:</h3>
      <table>
        <tr>
          <th>Nb</th>
          <th>Desc</th>
          <th>Ingredient List</th>
        </tr>
        {steps.map((c: Step) => (
          <>
            <tr>
              <th>{c.n.toString()}</th>
              <th>{c.description}</th>
              <th>{c.ingredientList}</th>
            </tr>
          </>
        ))}
      </table>

      <h3>Calorie Count: {calories}</h3>
      <button type="submit" onClick={() => addRecipe()}>
        Add
      </button>

      <button type="submit" onClick={() => goBack()}>
        Go back
      </button>
    </>
  );
};

export default ReviewPage;
