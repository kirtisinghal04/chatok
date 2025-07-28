async function sendMessage() {
    let inputField = document.getElementById("user-input");
    let message = inputField.value.trim();

    if (!message) return;

    // Append user message to chat box
    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="user-message"><strong>You:</strong> ${message}</div>`;

    inputField.value = "";

    try {
        let response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        });

        let data = await response.json();
        let botReply = data.reply || "Error getting response";

        chatBox.innerHTML += `<div class="bot-message"><strong>Bot:</strong> ${botReply}</div>`;
    } catch (error) {
        console.error("Chatbot Error:", error);
        chatBox.innerHTML += `<div class="bot-message">Oops! Something went wrong.</div>`;
    }
}

// Allows sending messages using Enter key
function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}
