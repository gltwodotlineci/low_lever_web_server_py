
document.addEventListener('deviceready', () => {
    // Cordova is now initialized. Have fun!
    window.location = "http://192.168.1.12:9998/"
    console.log('Running cordova-' + cordova.platformId + '@' + cordova.version);
}, false);
function alert_test(){
    alert("Salut")
}
