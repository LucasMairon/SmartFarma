/* eslint-disable no-unused-vars */
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import styles from './styles.module.css'; // Importando o CSS para estilo

const ProductsList = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [errorMessage, setErrorMessage] = useState('');

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get('https://api.escuelajs.co/api/v1/products');
                setProducts(response.data.slice(0, 12)); // Limitando a 12 produtos
            } catch (error) {
                setErrorMessage('Erro ao carregar produtos: ' + (error.response ? error.response.data : error.message));
            } finally {
                setLoading(false);
            }
        };

        fetchProducts();
    }, []);

    if (loading) return <div className={styles.loading}>Carregando produtos...</div>;

    return (
        <div className={styles.productsListContainer}>
            <h1>Lista de Produtos</h1>
            {errorMessage && <div className={styles.errorMessage}>{errorMessage}</div>}
            <div className={styles.productsList}>
                {products.map((product) => (
                    <div key={product.id} className={styles.productCard}>
                        <img src={product.images[0]} alt={product.title} className={styles.productImage} />
                        <h2 className={styles.productTitle}>{product.title}</h2>
                        <p className={styles.productDescription}>{product.description}</p>
                        <p className={styles.productPrice}>Preço: R$ {product.price}</p>
                        <p className={styles.productCategory}>Categoria: {product.category.name}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ProductsList;