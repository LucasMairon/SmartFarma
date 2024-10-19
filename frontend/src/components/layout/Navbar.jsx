// Navbar.js
import styles from "./Navbar.module.css";
import logo from "../../img/painkiller.png";
import { Link } from "react-router-dom";
import Container from "./Container";

function Navbar() {
  return (
    <nav className={styles.navbar}>
      <Container>
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
            <Link to="/Login">Login</Link>
          </li>
        </ul>
      </Container>
    </nav>
  );
}

export default Navbar;