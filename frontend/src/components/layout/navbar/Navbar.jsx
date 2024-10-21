// Navbar.js
import styles from "./navbar.module.css";
import logo from "../../../img/painkiller.png";
import { Link } from "react-router-dom";
// import Container from "./Container";

function Navbar() {
  return (
    <div className={styles.header}>
      <nav className={styles.navbar}>
        <Link to="/">
          <img src={logo} alt="SmartFarma Logo" />
        </Link>
        <ul className={styles.list}>
          <li className={styles.item}>
            <Link to="/">Home</Link>
          </li>
          <li className={styles.item}>
            <Link to="/Comprar">Comprar</Link>
          </li>
          <li className={styles.item}>
            <Link to="/products">Listar Produtos</Link>
          </li>
          <li className={styles.item}>
            <Link to="/add-product">Add Produtos</Link>
          </li>
          <li className={styles.item}>
            <Link to="/signin">Sign In</Link>
          </li>
          <li className={styles.item}>
            <Link to="/signup">Sign Up</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Navbar;
