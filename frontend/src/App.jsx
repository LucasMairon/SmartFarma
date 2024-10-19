import "./App.css";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Home from "./components/pages/Home/Home";
import Login from "./components/pages/Login/Login";
import Comprar from "./components/pages/Comprar/Comprar";
import Container from "./components/layout/Container";
import Navbar from "./components/layout/Navbar" // cabeçalho
import Footer from "./components/layout/Footer" // rodapé


// Digite rafce (React Arrow Function Component Export)

function App() {
  return (
    <Router>
      < Navbar/>
      <Container customClass="min-height">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Comprar" element={<Comprar />} />
          <Route path="/Login" element={<Login />} />
        </Routes>
      </Container>
      < Footer/> 
    </Router>
  );
}

export default App;
