import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import LoginPage from "./pages/login";
// import HomePage from "./pages/homepage";
import TitlePage from "./pages/titlepage";
import StepBuilderPage from "./pages/stepBuilderpage";
import ReviewPage from "./pages/reviewpage";

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
