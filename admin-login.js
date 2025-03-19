function adminLogin() {
    let username = document.getElementById("adminUsername").value;
    let password = document.getElementById("adminPassword").value;
    let errorMsg = document.getElementById("loginError");

    if (username === "admin" && password === "password123") {
        window.location.href = "admin-dashboard.html"; // Redirect to admin dashboard
    } else {
        errorMsg.textContent = "Invalid credentials. Try again!";
    }
}
