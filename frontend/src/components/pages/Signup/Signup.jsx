import { useState } from 'react';
import axios from 'axios';
import "./signup.module.css";

const Signup = () => {
  const [userData, setUserData] = useState({
    name: '',
    email: '',
    cpf: '',
    date_of_birth: '',
    phone_number: '',
    street: '',  // Campos de endereço diretamente no usuário
    city: '',
    state: '',
    number: '',
    neighborhood: '',
    complement: '',
    reference_point: '',
    zip_code: '',
    password: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUserData({ ...userData, [name]: value });
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
        street: userData.street,  // Campos de endereço agora estão aqui
        city: userData.city,
        state: userData.state,
        number: userData.number,
        neighborhood: userData.neighborhood,
        complement: userData.complement,
        reference_point: userData.reference_point,
        zip_code: userData.zip_code,
        password: userData.password,
      });

      console.log('Usuário criado:', userResponse.data);
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
        <input type="text" name="street" value={userData.street} onChange={handleInputChange} required />

        <label>Cidade:</label>
        <input type="text" name="city" value={userData.city} onChange={handleInputChange} required />

        <label>Estado:</label>
        <input type="text" name="state" value={userData.state} onChange={handleInputChange} required />

        <label>Número:</label>
        <input type="text" name="number" value={userData.number} onChange={handleInputChange} required />

        <label>Bairro:</label>
        <input type="text" name="neighborhood" value={userData.neighborhood} onChange={handleInputChange} required />

        <label>Complemento:</label>
        <input type="text" name="complement" value={userData.complement} onChange={handleInputChange} />

        <label>Ponto de Referência:</label>
        <input type="text" name="reference_point" value={userData.reference_point} onChange={handleInputChange} />

        <label>CEP:</label>
        <input type="text" name="zip_code" value={userData.zip_code} onChange={handleInputChange} required />

        <label>Senha:</label>
        <input type="text" name="password" value={userData.password} onChange={handleInputChange} required />

        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
};

export default Signup;