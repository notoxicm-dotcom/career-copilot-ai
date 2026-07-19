import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: `${API_URL}/api`,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const registerUser = (data: any) =>
  api.post('/auth/register', data).then((res) => res.data);

export const loginUser = (data: any) =>
  api.post('/auth/login', data).then((res) => res.data);

export const getCurrentUser = () =>
  api.get('/users/me').then((res) => res.data);

export const logoutUser = () => {
  localStorage.removeItem('token');
  return Promise.resolve();
};

export const uploadResume = (formData: FormData) =>
  api.post('/resumes/upload', formData).then((res) => res.data);

export const analyzeResume = (resumeId: number) =>
  api.post(`/resumes/analyze?resume_id=${resumeId}`).then((res) => res.data);

export const startInterview = (data: any) =>
  api.post('/interviews/start', data).then((res) => res.data);

export const searchVacancies = (query: string) =>
  api.get(`/vacancies?query=${query}`).then((res) => res.data);
