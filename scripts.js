document.getElementById('url-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const urlInput = document.getElementById('url-input').value;

    fetch('/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: urlInput })
    })
    .then(response => response.json())
    .then(data => {
        const result = document.getElementById('result');
        result.innerHTML = `Short URL: <a href="${window.location.href}${data.short_url}" target="_blank">${window.location.href}${data.short_url}</a>`;
    })
    .catch(error => {
        console.error('Error:', error);
        const result = document.getElementById('result');
        result.textContent = 'An error occurred. Please try again.';
    });
});
