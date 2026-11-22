import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "./styles.css";

export type Step = {
  n: number;
  description: string;
  ingredientList: string[];
};

const StepBuilderPage = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const user = location.state?.user;
  const title = location.state?.title;
  const steps = location.state?.steps;
  //   console.log(steps);

  //   const ingredients = location.state?.ingredients;
  const [stepIngredients, setStepIngredients] = useState<string[]>([]);
  const [allIngredients, setAllIngredients] = useState<any[]>([]);
  const [allStepIngredients, setAllStepIngredients] = useState<any[]>([]);
  const [newSteps, setNewSteps] = useState<Step[]>(steps);
  const [index, setIndex] = useState(1);
  const [description, setDescription] = useState("");

  useEffect(() => {
    if (steps && steps.length > 0) {
      const idx = steps[steps.length - 1].n + 1;
      setIndex(idx);
    }
  }, [steps]);

  const goNext = () => {
    if (title && newSteps) {
      //   const uniqueIngredients = Array.from(new Set(allStepIngredients));
      //   console.log(allStepIngredients);
      navigate("/review", {
        state: {
          user: user,
          title: title,
          steps: newSteps,
          //   ingredients: allStepIngredients,
        },
      });
    }
  };

  useEffect(() => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getIngredients`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setAllIngredients(result);
      });
  }, []);

  const handleChange = (ingredient: any, checked: boolean) => {
    if (checked) {
      setStepIngredients((prev) => [...prev, " ", ingredient.name]);
      //   setAllStepIngredients((prev) => [...prev, ingredient]);
    } else {
      setStepIngredients((prev) => prev.filter((i) => i != ingredient.name));
      //   setAllStepIngredients((prev) => prev.filter((i) => i != ingredient));
    }
  };

  const addStep = () => {
    setIndex(index + 1);
    const newStep: Step = {
      n: index,
      description: description,
      ingredientList: stepIngredients,
    };

    setNewSteps((prev) => [...prev, newStep]);
    // setAllStepIngredients((prev) => [...prev, newStep.ingredientList]);
  };

  const removeStep = (c: Step) => {
    setNewSteps((prev) => prev.filter((s) => s != c));
    newSteps.forEach((step) => {
      if (step.n >= c.n) {
        let idx = step.n - 1;
        step.n = idx;
      }
    });
  };

  return (
    <>
      <h2>Step Builder</h2>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          addStep();
        }}
      >
        <label>Description:</label>
        <input
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        {allIngredients.map((i) => (
          <>
            <input
              type="checkbox"
              name={i.name}
              checked={stepIngredients.includes(i.name)}
              onChange={(e) => handleChange(i, e.target.checked)}
            />
            {i.name}
          </>
        ))}

        <button type="submit">Add</button>
      </form>

      <table>
        <tr>
          <th>Nb</th>
          <th>Desc</th>
          <th>Ingredient List</th>
          <th>Action</th>
        </tr>
        {newSteps.map((c: Step) => (
          <>
            <tr>
              <th>{c.n.toString()}</th>
              <th>{c.description}</th>
              <th>{c.ingredientList}</th>
              <th>
                <button type="submit" onClick={() => removeStep(c)}>
                  remove
                </button>
              </th>
            </tr>
          </>
        ))}
      </table>

      <br></br>
      <button type="submit" onClick={() => goNext()}>
        Next
      </button>
    </>
  );
};

export default StepBuilderPage;
