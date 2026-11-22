// import { useState } from "react";
// import reactLogo from "./assets/react.svg";
// import viteLogo from "./assets/vite.svg";
// import heroImg from "./assets/hero.png";
import "./App.css";
import NewestPage from "./components/NewestPage";
import NewestSilliesSketch from "./components/NewestSilliesSketch";
import ImagePreview from "./components/ImagePreview";
import ComicPage from "./components/ComicPage";
import CharacterCard from "./components/CharacterCard";
import QnACard from "./components/QnACard";
import WantMoreBanner from "./components/WantMoreBanner";
import HomePage from "./pages/HomePage";
import CharacterIndexPage from "./pages/CharacterIndexPage";
import ContactCard from "./components/ContactCard";
import AboutPage from "./pages/AboutPage";
import SketchesPage from "./pages/SketchesPage";
import CharacterIndexTable, {
  type CharacterType,
} from "./components/CharacterIndexTable";
import ChaptersPage from "./pages/ChaptersPage";
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import { createRoot } from "react-dom/client";
import MainLayout from "./layouts/MainLayout";
import CharacterIndexTablePage from "./pages/CharacterIndexTablePage";
import UserProfileInfo from "./components/UserProfileInfo";
import UserProfilePage from "./pages/UserProfilePage";
import UserProfileEdit from "./components/UserProfileEdit";
import SilliesPage from "./pages/SilliesPage";

const characters: Array<CharacterType> = [
  {
    name: "Knightu ba",
    nickname: "Knightu ba",
    age: 28,
    job: "..knight gen",
    image: "../assets/hero.png",
  },
  {
    name: "Knightu ba",
    nickname: "Knightu ba",
    age: 28,
    job: "..knight gen",
    image: "../assets/hero.png",
  },
  {
    name: "Knightu ba",
    nickname: "Knightu ba",
    age: 28,
    job: "..knight gen",
    image: "../assets/hero.png",
  },
  {
    name: "Knightu ba",
    nickname: "Knightu ba",
    age: 28,
    job: "..knight gen",
    image: "../assets/hero.png",
  },
];

const isAdmin = true;
const username = "claylex-shipper73";
const description = "pretindem ca scrie ceva acia";
const pfpImg = "../public/knightref.png";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<MainLayout />}>
      <Route index element={<HomePage />} />
      <Route path="/chapters" element={<ChaptersPage />} />
      <Route
        path="/character-index"
        element={
          <CharacterIndexPage isAdmin={isAdmin} characterList={characters} />
        }
      />
      <Route
        path="/character-index-table"
        element={<CharacterIndexTablePage />}
      />

      <Route
        path="/profile"
        element={
          <UserProfilePage
            username={username}
            description={description}
            pfpImg={pfpImg}
          />
        }
      />

      <Route path="/sketches" element={<SketchesPage />} />
      <Route path="/sillies" element={<SilliesPage />} />
      <Route path="/about" element={<AboutPage />} />

      {/* <Route path="edit-profile" element={} */}
    </Route>,
  ),
);

function App() {
  // const [count, setCount] = useState(0);

  return (
    <>
      <RouterProvider router={router} />
      {/* <UserProfileInfo /> */}
      {/* <NewestPage></NewestPage>
      <NewestSilliesSketch></NewestSilliesSketch>
      <ImagePreview />
      <ComicPage />
      <CharacterCard />
      <QnACard></QnACard>
      <WantMoreBanner /> */}
      {/* <UserProfilePage /> */}
      {/* <UserProfileEdit /> */}

      {/* <HomePage /> */}
      {/* <CharacterIndexPageAdmin isAdmin={isAdmin} characterList={characters} /> */}
      {/* <ContactCard /> */}
      {/* <AboutPage /> */}
      {/* <SketchesPage /> */}
      {/* <CharacterIndexTable /> */}
      {/* <ChaptersPage /> */}

      {/* <section id="center">
        <div className="hero">
          <img src={heroImg} className="base" width="170" height="179" alt="" />
          <img src={reactLogo} className="framework" alt="React logo" />
          <img src={viteLogo} className="vite" alt="Vite logo" />
        </div>
        <div>
          <h1>Get started</h1>
          <p>
            Edit <code>src/App.tsx</code> and save to test <code>HMR</code>
          </p>
        </div>
        <button
          className="counter"
          onClick={() => setCount((count) => count + 1)}
        >
          Count is {count}
        </button>
      </section>

      <div className="ticks"></div>

      <section id="next-steps">
        <div id="docs">
          <svg className="icon" role="presentation" aria-hidden="true">
            <use href="/icons.svg#documentation-icon"></use>
          </svg>
          <h2>Documentation</h2>
          <p>Your questions, answered</p>
          <ul>
            <li>
              <a href="https://vite.dev/" target="_blank">
                <img className="logo" src={viteLogo} alt="" />
                Explore Vite
              </a>
            </li>
            <li>
              <a href="https://react.dev/" target="_blank">
                <img className="button-icon" src={reactLogo} alt="" />
                Learn more
              </a>
            </li>
          </ul>
        </div>
        <div id="social">
          <svg className="icon" role="presentation" aria-hidden="true">
            <use href="/icons.svg#social-icon"></use>
          </svg>
          <h2>Connect with us</h2>
          <p>Join the Vite community</p>
          <ul>
            <li>
              <a href="https://github.com/vitejs/vite" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#github-icon"></use>
                </svg>
                GitHub
              </a>
            </li>
            <li>
              <a href="https://chat.vite.dev/" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#discord-icon"></use>
                </svg>
                Discord
              </a>
            </li>
            <li>
              <a href="https://x.com/vite_js" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#x-icon"></use>
                </svg>
                X.com
              </a>
            </li>
            <li>
              <a href="https://bsky.app/profile/vite.dev" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#bluesky-icon"></use>
                </svg>
                Bluesky
              </a>
            </li>
          </ul>
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section> */}
    </>
  );
}

export default App;
