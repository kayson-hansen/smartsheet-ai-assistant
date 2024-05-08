function fetchChatHistory() {
  // Make a request to your backend API to fetch chat history
  // Replace 'YOUR_BACKEND_ENDPOINT' with your actual endpoint
  fetch('YOUR_BACKEND_ENDPOINT')
    .then(response => response.json())
    .then(data => {
      let chatHistory = document.getElementById('chat-history');
      chatHistory.innerHTML = ''; // Clear existing content

      // Display the chat history
      data.forEach(entry => {
        let message = document.createElement('div');
        message.textContent = entry.text;
        chatHistory.appendChild(message);
      });
    })
    .catch(error => {
      console.error('Error fetching chat history:', error);
    });
}

document.addEventListener('DOMContentLoaded', function () {
  fetchChatHistory();
});
