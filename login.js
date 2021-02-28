const LOGINSVCURL = "https://1v6h7vbzle.execute-api.us-east-1.amazonaws.com/dev";
const USERINFOSVCURL = "https://f9eibh3avi.execute-api.us-east-1.amazonaws.com/dev";

function init() {
    const usernameInput = document.getElementById("username");
    const username = usernameInput.value;

    const passwordInput = document.getElementById("password");
    const password = passwordInput.value;

    const logInBtn = document.getElementById("loginBtn");
    logInBtn.onclick = function() {
        logIn(username, password, false);
    };

    const signUpBtn = document.getElementById("signupBtn");
    signUpBtn.onclick = function() {
        logIn(username, password, true);
    };
}

function logIn(username, password, isNewUser) {
    if(isNewUser) {
        console.log(`Logging in user for the first time w/ credentials, u: ${username} p: ${password}`);
    }
    else {
        console.log(`Logging in existent user w/ credentials, u: ${username} p: ${password}`);
    }

    fetch(LOGINSVCURL, {
            "body": JSON.stringify({"username": username, "password": password}),
            "method": "POST"
    	})
        .then(getResponseBody)
        .then(function(response) {
	    const signUpSuccessful = response.addedSuccessful;
	    console.log(signUpSuccessful);
            if(signUpSuccessful) {
                alert("login successful");
		getUserInformation(username);
            }
            else {
                alert("already signed up");
            }
        });
}

function getUserInformation(username) {
    console.log(`Retrieving account information for username ${username}`)
    fetch(USERINFOSVCURL, {
	    "body": JSON.stringify({"username": username}),
	    "method": "POST"
    })
    .then(getResponseBody)
    .then(function(response) {
        const userInfoRetrievalSuccessful = response.successful;
        console.log(userInfoRetrievalSuccessful);
        if(userInfoRetrievalSuccessful) {
            alert("user info retrieval successful");
	}
	else {
            alert("user info retrieval not successful");
        }
    });
}

function getResponseBody(response) {
    if(response.status >= 200 && response.status < 300) {
        return Promise.resolve(response.json());
    }
    else {
	alert("error in response");
        return Promise.reject(new Error(response.statusText));
    } 
}

function signUp(username, password) {
    fetch(LOGINSVCURL, {
            "body": JSON.stringify({"username": username, "password": password}),
            "method": "POST"
    	})
        .then(getResponseBody)
        .then(function(response) {
	    const signUpSuccessful = response.addedSuccessful;
	    console.log(signUpSuccessful);
            if(signUpSuccessful) {
                alert("sign up successful");
            }
            else {
                alert("already signed up");
            }
        });
}

function displayTestCreationEnv() {
    // Personalize page
}

document.addEventListener("DOMContentLoaded", function(event) {
    init();
});
