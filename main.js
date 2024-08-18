document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    // Cordova is now initialized. Have fun!
       
    console.log('Running cordova-' + cordova.platformId + '@' + cordova.version);
    document.getElementById('deviceready').classList.add('ready');
}

//Storing values:
const default_values = {
    'key1': {"value1":"4","value2":"5"},
}

function set_value(key,value){
    /*Only accepts a json value*/
    localStorage.setItem(key, JSON.stringify(value));
}

function get_value(key){
    check_default(key);
    let value = localStorage.getItem(key);
    let parsedValue;
    try {
        parsedValue = JSON.parse(value);
        console.log(parsedValue); // Logs the JavaScript object
    } catch (error) {
        console.error('Error parsing JSON:', error);
    }
    return parsedValue;
}


/*Other functions you shouldn't touch*/
function check_default(key){
    let raw_value = localStorage.getItem(key);
    if (raw_value === 'NaN' || raw_value === 'null' || raw_value === null) {
        localStorage.setItem(key, JSON.stringify(default_values[key]));
    }
}

