import styles from "./Container.module.css";
import PropTypes from 'prop-types';

function Container(props) {
  return <div className={`${styles.container} ${styles.content}`}>{props.children}</div>;
}

Container.propTypes = {
  children: PropTypes.node.isRequired, // Define que "children" é obrigatório e deve ser um nó (qualquer coisa renderizável)
};

export default Container;