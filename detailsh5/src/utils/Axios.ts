import axios, { AxiosRequestConfig } from 'axios';

const axiosConfig: AxiosRequestConfig = {
  baseURL: 'http://8.130.40.39:8000/api', // api的base URL
  // baseURL : 'http://127.0.0.1:5000/api/',
  timeout: 5000, // 设置请求超时时间
  responseType: 'json',
  withCredentials: true, // 是否允许带cookie这些
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Access-Control-Allow-Origin': '*',
  },
};

// 创建axios实例
const axiosInstance = axios.create(axiosConfig);

axiosInstance.interceptors.request.use(
  (config) => {
    const access_token = localStorage.getItem('Authorization') // 假设你的token存在localStorage中
    if (access_token != null)
      config.headers['Authorization'] = access_token
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

export { axiosInstance, axiosConfig };
