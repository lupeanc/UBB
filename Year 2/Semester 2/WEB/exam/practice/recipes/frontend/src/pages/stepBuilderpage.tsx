import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

export type Step = {
  description: string;
  ingredients: string[];
};

const StepBuilderPage = () => {
  const location = useLocation();
  const user = location.state?.user;
  const title = location.state?.title;
  const gotSteps = location.state?.steps;
  const navigate = useNavigate();
  console.log(gotSteps);

  const [steps, setSteps] = useState<any[]>(gotSteps);
  // const [step, setStep] = useState("");
  const [description, setDescription] = useState("");
  const [ingredients, setIngredients] = useState<any[]>([]);
  const [stepIngredients, setStepIngredients] = useState<string[]>([]);
  const newStep: Step = {
    description: description,
    ingredients: stepIngredients,
  };

  useEffect(() => {
    fetch(
      `http://localhost:8000/controller/Controller.php?action=getIngredients`,
    )
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        setIngredients(result);
        // ingredients.forEach((e) => {
        //   stepIngredients.push(e.name);
        // });
      });
  }, []);

  const goNext = () => {
    navigate("/review", { state: { user: user, title: title, steps: steps } });
  };

  const addStep = (step: Step) => {
    // steps.push(step);
    setSteps((prev) => [...prev, step]);
    // window.location.reload();
  };

  const removeStep = (step: string) => {
    let filteredSteps = steps.filter((s) => s != step);
    setSteps(filteredSteps);
    // window.location.reload();
  };

  const handleChange = (name: string, checked: boolean) => {
    if (checked) {
      setStepIngredients((prev) => [...prev, name]);
    } else {
      setStepIngredients((prev) => prev.filter((i) => i !== name));
    }
  };

  return (
    <>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          goNext();
        }}
      >
        <label>Description:</label>
        <input
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        ></input>
        {ingredients.map((i) => (
          <>
            <input
              type="checkbox"
              name={i.name}
              checked={stepIngredients.includes(i.name)}
              onChange={(e) => handleChange(i.name, e.target.checked)}
            />
            {i.name}
          </>
        ))}

        <button
          type="submit"
          onClick={(e) => {
            e.preventDefault();
            addStep(newStep);
          }}
        >
          Add step
        </button>
      </form>

      <table>
        <tr>
          <th>Description</th>
          <th>Ingredients</th>
          <th>Action</th>
        </tr>
        {steps.map((s) => (
          <>
            <tr>
              <th>{s.description}</th>
              <th>{s.ingredients}</th>
              <th>
                <button
                  type="submit"
                  onClick={(e) => {
                    e.preventDefault();
                    removeStep(s);
                  }}
                >
                  Remove
                </button>
              </th>
            </tr>
          </>
        ))}
      </table>

      <button
        type="submit"
        onClick={(e) => {
          e.preventDefault();
          goNext();
        }}
      >
        Next
      </button>
    </>
  );
};
export default StepBuilderPage;
