/* eslint-disable no-unused-vars */
import React, { useState } from 'react';
import axios from 'axios';
import './styles.css';

const AddProduct = () => {
    const [product, setProduct] = useState({
        name: '',
        price: '',
        available_quantity: '',
        description: '',
        brand: '',
        maker: '',
        weight: '',
        ean: '',
        sku: '',
        image: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setProduct({ ...product, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const token = localStorage.getItem('token');

            const response = await axios.post('http://localhost:8000/api/products/', product, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
            });

            console.log('Produto adicionado com sucesso:', response.data);
        } catch (error) {
            console.error('Erro ao adicionar produto:', error.response ? error.response.data : error.message);
        }
    };

    return (
        <div className="add-product-container">
            <h2>Adicionar Novo Produto</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" name="name" placeholder="Nome" onChange={handleChange} required />
                <input type="text" name="price" placeholder="Preço" onChange={handleChange} required />
                <input type="number" name="available_quantity" placeholder="Quantidade Disponível" onChange={handleChange} required />
                <input type="text" name="description" placeholder="Descrição" onChange={handleChange} required />
                <input type="text" name="brand" placeholder="Marca" onChange={handleChange} required />
                <input type="text" name="maker" placeholder="Fabricante" onChange={handleChange} required />
                <input type="text" name="weight" placeholder="Peso" onChange={handleChange} required />
                <input type="text" name="ean" placeholder="Código de Barras" onChange={handleChange} required />
                <input type="text" name="sku" placeholder="SKU" onChange={handleChange} required />
                <input type="url" name="image" placeholder="URL da Imagem" onChange={handleChange} required />
                <button type="submit">Adicionar Produto</button>
            </form>
        </div>
    );
};

export default AddProduct;