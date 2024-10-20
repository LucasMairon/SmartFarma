import styles from './row.module.css';

const Row = () => {
  return (
    <div className={styles.row}>
      <div className={styles.col2}>
        <h1>Give Your Workout<br />A New Style!</h1>
        <p>
          Success isnt always about greatness. Its about consistency.
          Consistent<br />hard work gains success. Greatness will come.
        </p>
        <a href="" className={styles.button}>Explore Now &#8594;</a>
      </div>
      <div className={styles.col2}>
        <img src="images/image1.png" alt="" />
      </div>
    </div>
  );
};

export default Row;
