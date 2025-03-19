document.addEventListener("DOMContentLoaded", function () {
    console.log("Dashboard Loaded");
});
function sendMessage() {
    var input = document.getElementById("chatInput");
    var message = input.value.trim();

    if (message !== "") {
        var chatBox = document.getElementById("chatBox");
        var newMessage = document.createElement("p");
        newMessage.textContent = message;
        chatBox.appendChild(newMessage);
        input.value = "";
        
        // Auto-scroll to the latest message
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}
