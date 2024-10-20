import { FaFacebook, FaInstagram, FaLinkedin } from "react-icons/fa";
import styles from "./footer.module.css";

function Footer() {
  return (
    <footer className={styles.footer}>
      <ul className={styles.social_list}>
        <li>
          <FaFacebook />
        </li>
        <li>
          <FaInstagram />
        </li>
        <li>
          <FaLinkedin />
        </li>
      </ul>
      <p className={styles.copy_right}>
        <span>SmartFarma</span> &copy; 2024
      </p>
    </footer>
  );
}

export default Footer;
