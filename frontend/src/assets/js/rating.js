import axios from 'axios';

axios.defaults.baseURL = 'http://0.0.0.0:5000/api';

let exports = {};

exports.requestRating = async(name) => {
    var rating

    var x = true
    while (x) {
        await axios.get('rating/' + name)
            .then(response => {
                rating = response.data.rating
                document.getElementById("rating").innerHTML = rating
            })
            .catch(err => {
                console.log(err)
                x = false
            })
        console.log(rating)
        await new Promise(resolve => setTimeout(resolve, 2000))
    }
}

function getRating(name) {
    var rating

    axios.get('rating/' + name)
        .then(response => {
            rating = response.data.rating
            document.getElementById("rating").innerHTML = rating
        })
        .catch(err => {
            console.log(err)
        })
}

exports.uprate = (name) => {
    axios.get('uprate/' + name, { withCredentials: true })
        .then(response => {
            console.log(response)
            getRating(name);
        })
        .catch(err => {
            console.log(err)
        })
}

exports.downrate = (name) => {
    axios.get('downrate/' + name, { withCredentials: true })
        .then(response => {
            console.log(response)
            getRating(name);
        })
        .catch(err => {
            console.log(err)
        })
}

export default exports