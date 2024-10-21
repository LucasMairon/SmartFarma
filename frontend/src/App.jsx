import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
// components import
import Footer from "./components/layout/footer/Footer";
import Container from "./components/layout/container/Container";
import Navbar from "./components/layout/navbar/Navbar";
// import Header from "./components/layout/header/Header";

// pages import
import Home from "./components/pages/Home/Home";
import Signin from "./components/pages/Signin/signin";
import Comprar from "./components/pages/Comprar/Comprar";
import ProductList from "./components/pages/ProductList/ProductList";
import AddProduct from "./components/pages/AddProduct/AddProduct";
import Signup from "./components/pages/Signup/Signup";

function App() {
  return (
    <Router>
      < Navbar/>
      <Container customClass="min-height">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Comprar" element={<Comprar />} />
          <Route path="/signin" element={<Signin />} />
          <Route path="/signup" element={<Signup/>} />
          <Route path="/products" element={<ProductList />} />
          <Route path="/add-product" element={<AddProduct />} />
        </Routes>
      </Container>
      < Footer/> 
    </Router>
  );
}

export default App;
