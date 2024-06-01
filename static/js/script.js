document.getElementById('searchBtn').addEventListener('click', function() {
    const walletAddress = document.getElementById('walletAddress').value;
    if(walletAddress) {
        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `walletAddress=${walletAddress}`
        })
        .then(response => response.json())
        .then(data => {
            const statsSection = document.getElementById('stats');
            statsSection.innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please enter a wallet address');
    }
});
