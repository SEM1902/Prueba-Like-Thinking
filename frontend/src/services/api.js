import axios from 'axios';

let apiUrl = process.env.REACT_APP_API_URL;

if (!apiUrl) {
  if (process.env.NODE_ENV === 'production') {
    apiUrl = ''; // Use relative paths in production (served by same origin)
  } else {
    apiUrl = 'http://localhost:8000'; // Default for local dev
  }
}

if (apiUrl && !apiUrl.startsWith('http') && apiUrl !== '') {
  apiUrl = `https://${apiUrl}`;
}

const api = axios.create({
  baseURL: apiUrl,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para agregar token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Interceptor para manejar errores
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;

