import styles from "./home.module.css";

function Home() {
  return (
    <section className={styles.home}>
      <div className={styles.banner}>
        <h1>Bem-vindo à SmartFarma</h1>
        <p>Os melhores medicamentos, na palma da sua mão!</p>
      </div>

      <div className={styles.sectionHighlight}>
        <h2>Produtos em Destaque</h2>
        <div className={styles.products}>
          <div className={styles.product}>
            <img src="produto1.jpg" alt="Produto 1" />
            <h3>Produto 1</h3>
            <p>R$ 59,90</p>
            <button>Comprar</button>
          </div>
          <div className={styles.product}>
            <img src="produto2.jpg" alt="Produto 2" />
            <h3>Produto 2</h3>
            <p>R$ 29,90</p>
            <button>Comprar</button>
          </div>
          <div className={styles.product}>
            <img src="produto3.jpg" alt="Produto 3" />
            <h3>Produto 3</h3>
            <p>R$ 89,90</p>
            <button>Comprar</button>
          </div>
        </div>
      </div>

      <div className={styles.promoSection}>
        <h2>Promoções Especiais</h2>
        <p>
          Descontos de até <span>50%</span> em medicamentos selecionados!
        </p>
        <button>Ver Promoções</button>
      </div>
    </section>
  );
}

export default Home;
