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
            statsSection.innerHTML = '';
            Object.keys(data).forEach(key => {
                const statDiv = document.createElement('div');
                statDiv.className = 'stat';
                statDiv.innerHTML = `<strong>${key}:</strong> ${JSON.stringify(data[key], null, 2)}`;
                statsSection.appendChild(statDiv);
            });
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please enter a wallet address');
    }
});
