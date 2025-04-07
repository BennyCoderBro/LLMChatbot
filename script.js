window.onload = function() {
    initializeChat(); // Initialize chat with introduction
};

function initializeChat() {
    const introduction =
    "Hello! I am a chatbot built for Ascension Investment Management using LLM technology. I can answer questions like 'What is in Apple’s 10K report?' Feel free to ask me any questions!";
    addMessage("bot", introduction);
}

function sendMessage() {
    const userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return; // Exit if the input is empty

    addMessage("user", userInput); // Add user's message to the chat

    // Send a POST request to the server
    fetch("/process_input", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ input: userInput }) // Send user's input as JSON
    })
    .then(response => response.json())
    .then(data => {
        // Extract only the 'answer' key from the response
        const botResponse = data.answer || "I'm sorry, I don't understand.";
        addMessage("bot", botResponse);
    })
    .catch(error => {
        // Handle any network or server errors
        console.error("Error:", error);
        addMessage("bot", "Sorry, something went wrong. Please try again later.");
    });

    document.getElementById("user-input").value = ""; // Clear the input field
    document.getElementById("user-input").focus();   // Refocus the input field
}
function addMessage(sender, text) {
    const chatBox = document.getElementById("chat-box");
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", sender);
    messageDiv.innerText = text;
    messageDiv.setAttribute("role", "alert");       // Accessibility
    messageDiv.setAttribute("aria-live", "polite"); // Accessibility
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
}

function toggleChat() {
    const chatContainer = document.getElementById("chat-container");
    chatContainer.classList.toggle("hidden");

    // Change button icon
    const toggleIcon = document.getElementById("toggle-icon");
    if (chatContainer.classList.contains("hidden")) {
        toggleIcon.innerHTML = "💬"; // Chat closed
    }
}
