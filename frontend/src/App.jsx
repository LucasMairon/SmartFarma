import "./App.css";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Home from "./components/pages/Home/Home";
import Login from "./components/pages/Login/Login";
import Comprar from "./components/pages/Comprar/Comprar";
import Container from "./components/layout/Container";
import Navbar from "./components/layout/Navbar" // cabeçalho
import Footer from "./components/layout/Footer" // rodapé
import ProductList from "./components/pages/ProductList/ProductList";
import AddProduct from "./components/pages/AddProduct/AddProduct";

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
          <Route path="/products" element={<ProductList />} />
          <Route path="/add-product" element={<AddProduct />} />
        </Routes>
      </Container>
      < Footer/> 
    </Router>
  );
}

export default App;
