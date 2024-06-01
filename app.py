from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

def get_wallet_info(wallet_address, api_key):
    base_url = "https://api.basescan.org/api"
    endpoints = {
        "balance": f"{base_url}?module=account&action=balance&address={wallet_address}&apikey={api_key}",
        "txlist": f"{base_url}?module=account&action=txlist&address={wallet_address}&apikey={api_key}",
        "tokentx": f"{base_url}?module=account&action=tokentx&address={wallet_address}&apikey={api_key}",
        "tokennfttx": f"{base_url}?module=account&action=tokennfttx&address={wallet_address}&apikey={api_key}",
        "contract": f"{base_url}?module=contract&action=getcontractcreation&address={wallet_address}&apikey={api_key}",
        "gas": f"{base_url}?module=account&action=txlistinternal&address={wallet_address}&apikey={api_key}",
        "bridge": f"{base_url}?module=stats&action=bridgestats&address={wallet_address}&apikey={api_key}"
    }

    results = {}
    for key, url in endpoints.items():
        response = requests.get(url)
        if response.status_code == 200:
            results[key] = response.json()
        else:
            results[key] = {"error": f"Failed to fetch data, status code: {response.status_code}"}
    
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    wallet_address = request.form['walletAddress']
    api_key = "YourApiKey"  # Replace with your actual API key
    wallet_info = get_wallet_info(wallet_address, api_key)
    return jsonify(wallet_info)

if __name__ == '__main__':
    app.run(debug=True)
