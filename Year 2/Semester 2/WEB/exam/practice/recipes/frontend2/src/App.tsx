import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import LoginPage from "./pages/login";
import TitlePage from "./pages/titilepage";
import StepBuilderPage from "./pages/stepBuilderPage";
import ReviewPage from "./pages/reviewPage";
// import HomePage from "./pages/homepage";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route path="/title" element={<TitlePage />} />
          <Route path="/stepBuilder" element={<StepBuilderPage />} />
          <Route path="/review" element={<ReviewPage />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
