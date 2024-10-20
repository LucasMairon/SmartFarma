/* eslint-disable no-unused-vars */
import Row from '../row/Row';
import styles from './header.module.css';
import React, { useState } from 'react';

const Header = () => {
    // Estado para o toggle do menu
    const [menuHeight, setMenuHeight] = useState("0px");
  
    // Função de toggle do menu
    const menutoggle = () => {
      if (menuHeight === "0px") {
        setMenuHeight("200px");
      } else {
        setMenuHeight("0px");
      }
    };
  
    return (
      <div className={styles.header}>
        <div className={styles.container}>
          <div className={styles.navbar}>
            <div className={styles.logo}>
              <img src="images/logo.png" width="125px" alt="Logo" />
            </div>
            <nav>
              <ul id="MenuItems" className={styles.menuItems} style={{ maxHeight: menuHeight }}>
                <li><a href="">Home</a></li>
                <li><a href="">Products</a></li>
                <li><a href="">About</a></li>
                <li><a href="">Contact</a></li>
                <li><a href="">Account</a></li>
              </ul>
            </nav>
            <img src="images/cart.png" width="30px" height="30px" alt="Cart" />
            <img src="images/menu.png" className={styles.menuIcon} alt="Menu" onClick={menutoggle} />
          </div>
          <Row />
        </div>
      </div>
    );
  };
  
  export default Header;