document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const chatBox = document.getElementById('chat-box');

    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const userInput = document.getElementById('user-input').value;

        if (userInput) {
            chatBox.innerHTML += `<div class="user-message">${userInput}</div>`;
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `message=${userInput}`
            })
            .then(response => response.json())
            .then(data => {
                chatBox.innerHTML += `<div class="bot-response">${data.response}</div>`;
            });

            document.getElementById('user-input').value = '';
        }
    });
});
