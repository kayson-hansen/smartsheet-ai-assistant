// Create a chat widget element
const chatWidget = document.createElement('div');
chatWidget.style.position = 'fixed';
chatWidget.style.bottom = '20px';
chatWidget.style.right = '20px';
chatWidget.style.width = '60px';
chatWidget.style.height = '60px';
chatWidget.style.backgroundColor = 'lightblue';
chatWidget.style.borderRadius = '50%';
chatWidget.style.cursor = 'pointer';

// Create a pop-up window element
const popupWindow = document.createElement('div');
popupWindow.style.position = 'fixed';
popupWindow.style.bottom = '100px';
popupWindow.style.right = '100px';
popupWindow.style.width = '300px';
popupWindow.style.height = '400px';
popupWindow.style.backgroundColor = 'white';
popupWindow.style.display = 'none';

// Add chat widget to the webpage
document.body.appendChild(chatWidget);

// Add event listener to show/hide the pop-up window
chatWidget.addEventListener('click', () => {
  if (popupWindow.style.display === 'none') {
    popupWindow.style.display = 'block';
  } else {
    popupWindow.style.display = 'none';
  }
});

// Add event listener to close the pop-up window when clicking outside
document.addEventListener('click', (event) => {
  const target = event.target;
  if (target !== chatWidget && target !== popupWindow) {
    popupWindow.style.display = 'none';
  }
});

// Add chat interface to the pop-up window
popupWindow.innerHTML = `
  <div>
    <h1>Chat Interface</h1>
    <!-- Add your chat interface code here -->
  </div>
`;

// Add pop-up window to the webpage
document.body.appendChild(popupWindow);
