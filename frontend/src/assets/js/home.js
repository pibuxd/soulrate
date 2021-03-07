import axios from 'axios';

axios.defaults.baseURL = 'http://0.0.0.0:5000/api/';

let exports = {};

exports.requestRating = async() => {
    var x = true
    while (x) {
        await axios.get('home', { withCredentials: true })
            .then(response => {
                var rating = response.data.rating;
                var username = response.data.username
                document.getElementById("rating").innerHTML = rating
                document.getElementById("username").innerHTML = username
            })
            .catch(err => {
                console.log(err)
                x = false
            })

        await new Promise(resolve => setTimeout(resolve, 2000))
    }
}

export default exports