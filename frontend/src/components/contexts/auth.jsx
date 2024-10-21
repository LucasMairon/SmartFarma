/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import { createContext, useEffect, useState } from "react";
import axios from "axios";

export const AuthContext = createContext({});

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const userToken = localStorage.getItem("user_token");

    // Verifica se existe um token e tenta obter os dados do usuário
    if (userToken) {
      const fetchUserProfile = async () => {
        try {
          const response = await axios.get("http://localhost:8000/api/users/profile/", {
            headers: {
              Authorization: `Bearer ${JSON.parse(userToken).token}`,
            },
          });
          setUser(response.data); // Armazena os dados do usuário
        } catch (error) {
          console.error("Erro ao buscar perfil do usuário", error);
          localStorage.removeItem("user_token"); // Remove o token se houve erro
        }
      };
      fetchUserProfile();
    }
  }, []);

  const signin = async (email, password) => {
    try {
      const response = await axios.post("http://localhost:8000/api/token/", { email, password });
      const { access, refresh } = response.data;

      // Armazena os tokens no localStorage
      localStorage.setItem("user_token", JSON.stringify({ email, token: access }));

      // Busca o perfil do usuário após o login
      const profileResponse = await axios.get("http://localhost:8000/api/users/profile/", {
        headers: {
          Authorization: `Bearer ${access}`,
        },
      });

      setUser(profileResponse.data); // Armazena os dados do usuário

      return null; // Retorna null para indicar sucesso
    } catch (error) {
      console.error("Erro ao fazer login:", error);
      return "E-mail ou senha incorretos"; // Mensagem de erro
    }
  };

  const signup = async (email, password) => {
    try {
      const response = await axios.post("http://localhost:8000/api/users/", {
        email,
        password,
      });

      // Se o signup for bem-sucedido, você pode automaticamente fazer o login
      return await signin(email, password);
    } catch (error) {
      console.error("Erro ao cadastrar:", error);
      if (error.response && error.response.status === 400) {
        return "Já tem uma conta com esse E-mail"; // Mensagem de erro
      }
      return "Erro ao cadastrar. Tente novamente."; // Mensagem genérica
    }
  };

  const signout = () => {
    setUser(null);
    localStorage.removeItem("user_token");
  };

  return (
    <AuthContext.Provider
      value={{ user, signed: !!user, signin, signup, signout }}
    >
      {children}
    </AuthContext.Provider>
  );
};