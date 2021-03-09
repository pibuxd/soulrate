import axios from 'axios';

axios.defaults.baseURL = 'http://0.0.0.0:5000/api/';

let exports = {};

exports.requestHome = async() => {
    return (await axios.get('home', { withCredentials: true }))
        .data
}

export default exports