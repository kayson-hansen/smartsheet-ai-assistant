chrome.action.onClicked.addListener((tab) => {
  chrome.action.setPopup({ tabId: tab.id, popup: 'popup.html' });
});
