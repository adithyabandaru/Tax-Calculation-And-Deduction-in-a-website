const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = form.elements.username.value;
    const email = form.elements.email.value;
    const password = form.elements.password.value;
    const confirmPassword = form.elements['confirm-password'].value;

    // Check if the password and confirm password fields match
    if (password !== confirmPassword) {
        alert('Password and Confirm Password fields do not match!');
        return;
    }
    // Send a POST request to the server to create the user
    fetch('/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        })
        .then((response) => response.text())
        .then((data) => {
            alert(data);
            form.reset();
        })
        .catch((error) => {
            console.error(error);
        });
});