import { useState } from 'react';
import axios from 'axios';
import "./signup.module.css"

const Signup = () => {
  const [userData, setUserData] = useState({
    name: '',
    email: '',
    cpf: '',
    date_of_birth: '',
    phone_number: '',
    address: {
      street: '',
      city: '',
      state: '',
      number: '',
      neighborhood: '',
      complement: '',
      reference_point: '',
      zip_code: '',
    },
    password: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    if (name.includes('address.')) {
      const field = name.split('.')[1];
      setUserData({
        ...userData,
        address: { ...userData.address, [field]: value },
      });
    } else {
      setUserData({ ...userData, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Enviar dados do usuário
      const userResponse = await axios.post('http://localhost:8000/api/users/', {
        name: userData.name,
        email: userData.email,
        cpf: userData.cpf,
        date_of_birth: userData.date_of_birth,
        phone_number: userData.phone_number,
        password: userData.password,
        address: userData.address,
      });
      
      console.log('Usuário criado:', userResponse.data);
  
      // Enviar endereço separadamente
      const addressResponse = await axios.post('http://localhost:8000/api/addresses/', {
        user: userResponse.data.id, // ID do usuário criado
        street: userData.address.street,
        city: userData.address.city,
        state: userData.address.state,
        number: userData.address.number,
        neighborhood: userData.address.neighborhood,
        complement: userData.address.complement,
        reference_point: userData.address.reference_point,
        zip_code: userData.address.zip_code,
        is_default: true,
      });
  
      console.log('Endereço criado:', addressResponse.data);
      alert('Cadastro realizado com sucesso!');
    } catch (error) {
      if (error.response) {
        // O servidor respondeu com um código de erro
        console.error('Erro ao cadastrar usuário:', error.response.data);
      } else if (error.request) {
        // A requisição foi feita, mas não houve resposta
        console.error('Erro na requisição:', error.request);
      } else {
        // Alguma outra coisa deu errado ao configurar a requisição
        console.error('Erro desconhecido:', error.message);
      }
    }
  };
  

  return (
    <div className="signup-container">
      <h2>Cadastro de Usuário</h2>
      <form onSubmit={handleSubmit} className="signup-form">
        <label>Nome:</label>
        <input type="text" name="name" value={userData.name} onChange={handleInputChange} required />

        <label>Email:</label>
        <input type="email" name="email" value={userData.email} onChange={handleInputChange} required />

        <label>CPF:</label>
        <input type="text" name="cpf" value={userData.cpf} onChange={handleInputChange} required />

        <label>Data de Nascimento:</label>
        <input type="date" name="date_of_birth" value={userData.date_of_birth} onChange={handleInputChange} required />

        <label>Telefone:</label>
        <input type="text" name="phone_number" value={userData.phone_number} onChange={handleInputChange} required />

        <h3>Endereço</h3>

        <label>Rua:</label>
        <input type="text" name="address.street" value={userData.address.street} onChange={handleInputChange} required />

        <label>Cidade:</label>
        <input type="text" name="address.city" value={userData.address.city} onChange={handleInputChange} required />

        <label>Estado:</label>
        <input type="text" name="address.state" value={userData.address.state} onChange={handleInputChange} required />

        <label>Número:</label>
        <input type="text" name="address.number" value={userData.address.number} onChange={handleInputChange} required />

        <label>Bairro:</label>
        <input type="text" name="address.neighborhood" value={userData.address.neighborhood} onChange={handleInputChange} required />

        <label>Complemento:</label>
        <input type="text" name="address.complement" value={userData.address.complement} onChange={handleInputChange} />

        <label>Ponto de Referência:</label>
        <input type="text" name="address.reference_point" value={userData.address.reference_point} onChange={handleInputChange} />

        <label>CEP:</label>
        <input type="text" name="address.zip_code" value={userData.address.zip_code} onChange={handleInputChange} required />

        <label>Senha:</label>
        <input type="password" name="password" value={userData.password} onChange={handleInputChange} required />

        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
};

export default Signup;