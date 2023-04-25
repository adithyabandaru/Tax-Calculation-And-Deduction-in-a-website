document.addEventListener("DOMContentLoaded", () => {
    const loginButton = document.getElementById("login-btn");
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");

    loginButton.addEventListener("click", () => {
        const username = usernameInput.value;
        const password = passwordInput.value;

        // Make sure both fields are filled in
        if (!username || !password) {
            alert("Please enter a username and password.");
            return;
        }

        // Send a POST request to the login route
        fetch("/login", {
                method: "POST",
                body: JSON.stringify({ username, password }),
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Login successful!");
                    // Redirect to the home page
                    window.location.href = "indexh";
                } else {
                    alert("Login failed. Please check your username and password.");
                }
            })
            .catch(error => console.error(error));
    });
});