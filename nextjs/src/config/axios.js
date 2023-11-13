import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://app:8000',
  timeout: 5000, // Request timeout in milliseconds
});


export default axiosInstance;