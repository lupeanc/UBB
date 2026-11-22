import { render, screen, within } from "@testing-library/react";
import MainPage from "./pages/MainPage";

describe("MainPage", () => {
  it("renders without crashing", () => {
    render(<MainPage />);
  });

  it("renders NewestSilliesSketch components for silly and sketch", () => {
    render(<MainPage />);

    // Check the silly section
    const sillyDiv = screen.getByText(/NEWEST SILLY/i).closest("div");
    expect(sillyDiv).toBeInTheDocument();

    const sillyImg = within(sillyDiv!).getByAltText(""); // empty string
    expect(sillyImg).toHaveAttribute(
      "src",
      "../public/adventure-time-fart-noise.jpg",
    );

    const sillyDesc = within(sillyDiv!).getByText(
      /That one scary dog privillege \(im dyslexic idk how to spell that word\) trend/i,
    );
    expect(sillyDesc).toBeInTheDocument();

    // Check the sketch section
    const sketchDiv = screen.getByText(/NEWEST SKETCH/i).closest("div");
    expect(sketchDiv).toBeInTheDocument();

    const sketchImg = within(sketchDiv!).getByAltText(""); // the second img
    expect(sketchImg).toHaveAttribute("src", "../public/Prince&Tofu.png");

    const sketchDesc = within(sketchDiv!).getByText(
      /Doodle of Modern AU Prince and Tofu/i,
    );
    expect(sketchDesc).toBeInTheDocument();
  });
});
