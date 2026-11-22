import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import CharacterIndexTable from "./components/CharacterIndexTable";
import type { CharacterType } from "./pages/MainPage";
import { vi } from "vitest";

// Mock Image so isValidImage always resolves
(globalThis as any).Image = class {
  src = "";
  onload: () => void = () => {};
  onerror: () => void = () => {};
  constructor() {
    setTimeout(() => this.onload(), 0);
  }
};

const setup = (initialCharacters: CharacterType[] = []) => {
  const setCharacters = vi.fn();
  render(
    <CharacterIndexTable
      characters={initialCharacters}
      setCharacters={setCharacters}
    />,
  );
  return { setCharacters };
};

describe("CharacterIndexTable", () => {
  it("adds a new character", async () => {
    const { setCharacters } = setup();
    const user = userEvent.setup();

    await user.type(screen.getByPlaceholderText("Name"), "John");
    await user.type(screen.getByPlaceholderText("Nickname"), "Johnny");
    await user.type(screen.getByPlaceholderText("Age"), "30");
    await user.type(screen.getByPlaceholderText("Job"), "Dev");
    await user.type(screen.getByPlaceholderText("Image"), "/img.png");

    await user.click(screen.getByRole("button", { name: /Add/i }));

    // wait for async functions
    await new Promise((r) => setTimeout(r, 10));

    expect(setCharacters).toHaveBeenCalledWith([
      {
        name: "John",
        nickname: "Johnny",
        age: 30,
        job: "Dev",
        image: "/img.png",
      },
    ]);
  });

  it("validates age > 0", async () => {
    setup();
    const user = userEvent.setup();

    await user.type(screen.getByPlaceholderText("Name"), "John");
    await user.type(screen.getByPlaceholderText("Nickname"), "Johnny");
    await user.type(screen.getByPlaceholderText("Age"), "0");
    await user.type(screen.getByPlaceholderText("Job"), "Dev");
    await user.type(screen.getByPlaceholderText("Image"), "/img.png");

    await user.click(screen.getByRole("button", { name: /Add/i }));

    expect(
      await screen.findByText(/Age must be greater than 0/i),
    ).toBeInTheDocument();
  });

  it("shows error if required fields are empty", async () => {
    const { setCharacters } = setup();
    const user = userEvent.setup();

    await user.click(screen.getByRole("button", { name: /Add/i }));

    expect(
      await screen.findByText(/All fields are required/i),
    ).toBeInTheDocument();
    expect(setCharacters).not.toHaveBeenCalled();
  });

  it("renders characters in table", () => {
    const characters: CharacterType[] = [
      {
        name: "Test",
        nickname: "Nick",
        age: 20,
        job: "Job",
        image: "/img.png",
      },
    ];
    setup(characters);

    expect(screen.getByText("Test")).toBeInTheDocument();
  });

  it("removes a character", async () => {
    const characters: CharacterType[] = [
      {
        name: "Test",
        nickname: "Nick",
        age: 20,
        job: "Job",
        image: "/img.png",
      },
    ];
    const { setCharacters } = setup(characters);
    const user = userEvent.setup();

    await user.click(screen.getByText(/Remove/i));

    expect(setCharacters).toHaveBeenCalledWith([]);
  });

  it("edits an existing character", async () => {
    const characters: CharacterType[] = [
      {
        name: "John",
        nickname: "Johnny",
        age: 30,
        job: "Dev",
        image: "/img.png",
      },
    ];
    const { setCharacters } = setup(characters);
    const user = userEvent.setup();

    await user.click(screen.getByText("Edit"));

    // Wait for inputs to populate
    const nameInput = await screen.findByDisplayValue("John");
    const ageInput = screen.getByDisplayValue("30");

    await user.clear(nameInput);
    await user.type(nameInput, "Jane");
    await user.clear(ageInput);
    await user.type(ageInput, "25");

    await user.click(screen.getByRole("button", { name: /Update/i }));

    await new Promise((r) => setTimeout(r, 10));

    expect(setCharacters).toHaveBeenCalledWith([
      {
        name: "Jane",
        nickname: "Johnny",
        age: 25,
        job: "Dev",
        image: "/img.png",
      },
    ]);

    expect(screen.getByPlaceholderText("Name")).toHaveValue("");
    expect(screen.getByRole("button", { name: /Add/i })).toBeInTheDocument();
  });

  it("shows error if image is invalid", async () => {
    const { setCharacters } = setup();
    const user = userEvent.setup();

    (globalThis as any).Image = class {
      src = "";
      onload: () => void = () => {};
      onerror: () => void = () => {};
      constructor() {
        setTimeout(() => this.onerror(), 0);
      }
    };

    await user.type(screen.getByPlaceholderText("Name"), "John");
    await user.type(screen.getByPlaceholderText("Nickname"), "Johnny");
    await user.type(screen.getByPlaceholderText("Age"), "30");
    await user.type(screen.getByPlaceholderText("Job"), "Dev");
    await user.type(screen.getByPlaceholderText("Image"), "/bad.png");

    await user.click(screen.getByRole("button", { name: /Add/i }));
    await new Promise((r) => setTimeout(r, 10));

    expect(
      await screen.findByText(/Image path is invalid or cannot be loaded/i),
    ).toBeInTheDocument();
    expect(setCharacters).not.toHaveBeenCalled();
  });
});
