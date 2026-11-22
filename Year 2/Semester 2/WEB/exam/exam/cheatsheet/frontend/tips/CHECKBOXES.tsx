import { useState } from "react";

// const listOfSteps;
const [stepIngredients, setStepIngredients] = useState<string[]>([]);
const [allIngredients, setAllIngredients] = useState<any[]>([]);

{
  allIngredients.map((i) => (
    <>
      <input
        type="checkbox"
        name={i.name}
        checked={stepIngredients.includes(i.name)}
        onChange={(e) => handleChange(i, e.target.checked)}
      />
      {i.name}
    </>
  ));
}

const handleChange = (ingredient: any, checked: boolean) => {
  if (checked) {
    setStepIngredients((prev) => [...prev, " ", ingredient.name]);
  } else {
    setStepIngredients((prev) => prev.filter((i) => i != ingredient.name));
  }
};
