import axios from './configs/axios';

let exports = {};

/**
 * rating of the user
 * @param {*} name
 * @returns response.data from api/rating
 */
exports.requestRating = async(name) => {
    return (await axios.get('rating/' + name, { withCredentials: true }))
        .data
}

/**
 * uprate user's rating
 * @param {*} name 
 * @returns response code
 */
exports.uprate = async(name) => {
    return (await axios.get('uprate/' + name, { withCredentials: true }))
        .data
}

/**
 * downrate user's rating
 * @param {*} name 
 * @returns response code
 */
exports.downrate = async(name) => {
    return (await axios.get('downrate/' + name, { withCredentials: true }))
        .data
}

export default exports