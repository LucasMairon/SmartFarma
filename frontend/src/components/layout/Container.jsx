// Container.js
import styles from "./Container.module.css";
import PropTypes from 'prop-types';

function Container(props) {
  return (
    <div className={`${styles.container} ${props.customClass ? styles[props.customClass] : ''}`}>
      {props.children}
    </div>
  );
}

Container.propTypes = {
  children: PropTypes.node.isRequired,
  customClass: PropTypes.string, // Agora é opcional
};

export default Container;