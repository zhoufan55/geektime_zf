import axios from 'axios'

const http = axios.create({
    baseURL: 'http://192.168.1.14:5001',
    timeout: 1000,
    headers: { 'Authorization': "Bearer " + localStorage.token }
});

export default http