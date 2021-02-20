// login.js

function init() {
    const button = document.getElementById("loginBtn");

    button.onclick = function() {
        const usernameInput = document.getElementById("username");
        const username = usernameInput.value;

        const passwordInput = document.getElementById("password");
        const password = passwordInput.value;

        getUserInformation(username, password);
    };
}

function getUserInformation(username, password) {
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        const userId = xmlHttp.responseText;
        alert(userId);
    };

    xmlHttp.open("GET", "http://localhost:8080", true); 
    xmlHttp.send(null);
}

function displayTestCreationEnv() {
    // Personalize page
}

document.addEventListener("DOMContentLoaded", function(event) {
    init();
});
