import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // Importando useNavigate
import styles from './signin.module.css'; // Importando estilos do módulo CSS

const SignIn = () => {
  const [credentials, setCredentials] = useState({
    email: '',
    password: '',
  });

  const navigate = useNavigate(); // Hook para redirecionamento

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCredentials({ ...credentials, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        console.log("Tentando autenticar com:", credentials); // Adicionado para debug
        const response = await axios.post('http://localhost:8000/api/users/token/', {
            email: credentials.email,
            password: credentials.password,
        });

        console.log('Tokens:', response.data);
        alert('Login realizado com sucesso!');
        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        navigate('/dashboard');
    } catch (error) {
        if (error.response) {
            console.error('Erro ao fazer login:', error.response.data);
            alert('Erro ao fazer login: ' + error.response.data.detail);
        } else {
            console.error('Erro na requisição:', error);
            alert('Erro desconhecido. Tente novamente mais tarde.');
        }
    }
};


  return (
    <div className={styles.signinContainer}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit} className={styles.signinForm}>
        <label>Email:</label>
        <input 
          type="email" 
          name="email" 
          value={credentials.email} 
          onChange={handleInputChange} 
          required 
        />

        <label>Senha:</label>
        <input 
          type="password" 
          name="password" 
          value={credentials.password} 
          onChange={handleInputChange} 
          required 
        />

        <button type="submit">Entrar</button>
      </form>
    </div>
  );
};

export default SignIn;
