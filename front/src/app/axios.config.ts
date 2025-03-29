import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000',
});

// Intercepteur de requêtes : ajoute automatiquement le token
instance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default instance;
