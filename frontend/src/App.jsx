import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./components/pages/Home/Home";
import Login from "./components/pages/Login/Login";
import Comprar from "./components/pages/Comprar/Comprar";
import Container from "./components/layout/Container";

// Digite rafce (React Arrow Function Component Export)

function App() {
  return (
    <Router>
      <div>
        <Link to="/">Home</Link>
        <Link to="/Comprar">Comprar</Link>
        <Link to="/Login">Login</Link>
      </div>
      <Container customClass="content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Comprar" element={<Comprar />} />
          <Route path="/Login" element={<Login />} />
        </Routes>
      </Container>
      <p>footer</p>
    </Router>
  );
}

export default App;
