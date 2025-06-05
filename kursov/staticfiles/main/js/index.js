
const form = document.getElementById('form');
const input = document.getElementById('input');
const output = document.getElementById('output');
const error = document.getElementById('error');
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    output.value = '';
    error.textContent = '';
    const inputValue = input.value.trim();
    if (inputValue === '') {
        error.textContent = 'Please enter a valid URL.';
        return;
    }
    try {
        const response = await fetch('/api/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: inputValue })
        });
        if (!response.ok) {
            throw new Error('Failed to shorten URL');
        }
        const data = await response.json();
        output.value = data.shortened_url;
    } catch (err) {
        error.textContent = err.message;
    }
});
const copyButton = document.getElementById('copyButton');
copyButton.addEventListener('click', () => {
    const shortenedUrl = output.value;
    if (shortenedUrl) {
        navigator.clipboard.writeText(shortenedUrl).then(() => {
            alert('Shortened URL copied to clipboard!');
        }).catch(err => {
            console.error('Failed to copy: ', err);
        });
    } else {
        alert('No URL to copy.');
    }
});
const clearButton = document.getElementById('clearButton');
clearButton.addEventListener('click', () => {
    input.value = '';
    output.value = '';
    error.textContent = '';
});
const historyButton = document.getElementById('historyButton');
historyButton.addEventListener('click', async () => {
    try {
        const response = await fetch('/api/history');
        if (!response.ok) {
            throw new Error('Failed to fetch history');
        }
        const data = await response.json();
        const historyList = document.getElementById('historyList');
        historyList.innerHTML = '';
        data.history.forEach(item => {
            const listItem = document.createElement('li');
            listItem.textContent = `${item.original_url} - ${item.shortened_url}`;
            historyList.appendChild(listItem);
        });
    } catch (err) {
        error.textContent = err.message;
    }
});
const clearHistoryButton = document.getElementById('clearHistoryButton');
clearHistoryButton.addEventListener('click', async () => {
    try {
        const response = await fetch('/api/clear_history', {
            method: 'POST'
        });
        if (!response.ok) {
            throw new Error('Failed to clear history');
        }
        document.getElementById('historyList').innerHTML = '';
        alert('History cleared successfully!');
    } catch (err) {
        error.textContent = err.message;
    }
});
// Initialize the clipboard functionality
if (navigator.clipboard && navigator.clipboard.writeText) {
    console.log('Clipboard API is supported');
}
else {
    console.warn('Clipboard API is not supported in this browser');
}
// Check if the browser supports the Fetch API
if (window.fetch) {
    console.log('Fetch API is supported');
}
else {
    console.warn('Fetch API is not supported in this browser');
}
// Check if the browser supports Promises
if (window.Promise) {
    console.log('Promises are supported');
}
else {
    console.warn('Promises are not supported in this browser');
}
// Check if the browser supports async/await
if (window.async) {
    console.log('Async/Await is supported');
}
else {
    console.warn('Async/Await is not supported in this browser');
}
// Check if the browser supports localStorage
if (window.localStorage) {
    console.log('Local Storage is supported');
}
else {
    console.warn('Local Storage is not supported in this browser');
}
// Check if the browser supports sessionStorage
if (window.sessionStorage) {
    console.log('Session Storage is supported');
}
else {
    console.warn('Session Storage is not supported in this browser');
}
// Check if the browser supports Service Workers
if ('serviceWorker' in navigator) {
    console.log('Service Workers are supported');
}

const serviceWorkerRegistration = navigator.serviceWorker.register('/service-worker.js')
    .then(registration => {
        console.log('Service Worker registered with scope:', registration.scope);
    })
    .catch(error => {
        console.error('Service Worker registration failed:', error);
    });

// Check if the browser supports IndexedDB
if (window.indexedDB) {
    console.log('IndexedDB is supported');
}
else {
    console.warn('IndexedDB is not supported in this browser');
}
