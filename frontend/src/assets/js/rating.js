import axios from 'axios';

axios.defaults.baseURL = 'http://0.0.0.0:5000/api/';

let exports = {};

exports.requestRating = async(name) => {
    return (await axios.get('rating/' + name, { withCredentials: true }))
        .data
}

exports.uprate = async(name) => {
    return (await axios.get('uprate/' + name, { withCredentials: true }))
        .data
}

exports.downrate = async(name) => {
    return (await axios.get('downrate/' + name, { withCredentials: true }))
        .data
}

export default exports