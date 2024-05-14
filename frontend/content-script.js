import React, { useState } from 'react';
import ReactDOM from 'react-dom';

const App = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);

  const handleChatClick = () => {
    setIsOpen(!isOpen);
  };

  const handleSendMessage = async (messageText) => {
    // Send message to the API and receive a response
    const response = await fetch('localhost:8000/invoke', {
      method: 'POST',
      body: JSON.stringify({ input: messageText }),
      headers: {
        'Content-Type': 'application/json',
      },
    });
    const data = await response.json();

    // Create a new message bubble with the response text
    const newMessage = {
      id: messages.length + 1,
      text: data.response,
      user: { id: 'ai', name: 'AI Assistant' },
    };

    setMessages([...messages, newMessage]);
  };

  return (
    <div>
      <div
        style={{
          position: 'fixed',
          bottom: '20px',
          right: '20px',
          width: '60px',
          height: '60px',
          backgroundColor: 'lightblue',
          borderRadius: '50%',
          cursor: 'pointer',
        }}
        onClick={handleChatClick}
      >
        Chat
      </div>
      {isOpen && (
        <div
          style={{
            position: 'fixed',
            bottom: '100px',
            right: '100px',
            width: '300px',
            height: '400px',
            backgroundColor: 'white',
          }}
        >
          <div>
            <h1>Chat Interface</h1>
            <div>
              {messages.map((message) => (
                <div key={message.id}>{message.text}</div>
              ))}
            </div>
            <div>
              <input type="text" />
              <button onClick={() => handleSendMessage('Hello!')}>
                Send
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
