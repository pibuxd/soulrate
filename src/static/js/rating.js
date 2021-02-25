function uprate(name) {
    fetch(`/api/uprate/${name}`)
        .then(function(response) {
            return response.json();
        })
        .then(function(myJson) {
            console.log(myJson.did);
            getRating(name);
        })
        .catch(function(error) {
            console.log("Error: " + error);
        });
}

function downrate(name) {
    fetch(`/api/downrate/${name}`)
        .then(function(response) {
            return response.json();
        })
        .then(function(myJson) {
            console.log(myJson.did);
            getRating(name);
        })
        .catch(function(error) {
            console.log("Error: " + error);
        });
}

async function getRating(name) {
    fetch(`/api/rating/${name}`)
        .then(function(response) {
            return response.json();
        })
        .then(function(myJson) {
            document.getElementById("rating").innerHTML = myJson.rating
            console.log(myJson.rating);
        })
        .catch(function(error) {
            console.log("Error: " + error);
        });
}