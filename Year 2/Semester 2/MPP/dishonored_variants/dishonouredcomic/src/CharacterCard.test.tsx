import { render, screen } from "@testing-library/react";
import CharacterCard from "./components/CharacterCard";
import type { CharacterType } from "./pages/MainPage";
// import { vi } from "vitest";

const mockCharacter: CharacterType = {
  name: "Test Name",
  nickname: "Test Nick",
  age: 25,
  job: "Tester",
  image: "/assets/test.png",
};

describe("CharacterCard", () => {
  it("renders all character data", () => {
    render(<CharacterCard character={mockCharacter} />);

    expect(screen.getByText(/Test Name/)).toBeInTheDocument();
    expect(screen.getByText(/Test Nick/)).toBeInTheDocument();
    expect(screen.getByText(/25/)).toBeInTheDocument();
    expect(screen.getByText(/Tester/)).toBeInTheDocument();
  });

  it("renders image with correct src", () => {
    render(<CharacterCard character={mockCharacter} />);
    const img = screen.getByRole("img");

    expect(img).toHaveAttribute("src", mockCharacter.image);
  });
});
