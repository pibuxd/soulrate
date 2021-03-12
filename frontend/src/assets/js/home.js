import axios from './configs/axios';

let exports = {};

/**
 * data of the user
 * @returns response.data from api/home
 */
exports.requestHome = async() => {
    return (await axios.get('home', { withCredentials: true }))
        .data
}

export default exports