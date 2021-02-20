// login.js

function init() {
    const button = document.getElementById("loginBtn");

    button.onclick = function() {
        alert("logging in user");
        window.location.href = "upload.html";
    };
}

document.addEventListener("DOMContentLoaded", function(event) {
      // - Code to execute when all DOM content is loaded. 
      // - including fonts, images, etc.
    init();
});
