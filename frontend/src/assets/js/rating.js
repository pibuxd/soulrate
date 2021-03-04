/**
 * Uprates user and refresh rating value in id=rating (html)
 * @param {*} name user to uprate
 */
function uprate(name) {
    fetch(`/api/uprate/${name}`)
        .then(function(response) {
            return response.json();
        })
        .then(function(myJson) {
            //console.log(myJson.did);
            getRating(name);
        })
        .catch(function(error) {
            console.log("Error: " + error);
        });
}

/**
 * Downrates user and refresh rating value in id=rating (html)
 * @param {*} name user to downrate
 */
function downrate(name) {
    fetch(`/api/downrate/${name}`)
        .then(function(response) {
            return response.json();
        })
        .then(function(myJson) {
            //console.log(myJson.did);
            getRating(name);
        })
        .catch(function(error) {
            console.log("Error: " + error);
        });
}

/**
 * Prints rating value in id=rating (html)
 * @param {*} name user to print rating
 */
function getRating(name) {
    fetch(`/api/rating/${name}`)
        .then(function(response) {
            return response.json();
        })
        .then(function(myJson) {
            document.getElementById("rating").innerHTML = myJson.rating
                //console.log(myJson.rating);
        })
        .catch(function(error) {
            console.log("Error: " + error);
        });
}

/**
 * Prints every {interval} seconds rating value in id=rating (html)
 * @param {*} name user to print rating 
 * @param {*} interval change every value of seconds
 */
function getRatingEverySec(name, interval) {
    return new Promise(printRating => {
        setTimeout(() => {
            printRating(getRating(name));
        }, interval * 1000);
    });
}

/**
 * Async call of getRatingEverySec with interval
 * @param {*} name user to print rating
 * @param {*} interval every {interval} seconds call getRating
 */
async function asyncGetRating(name, interval) {
    while (true) {
        //console.log('calling rating');
        await getRatingEverySec(name, interval);
    }
}