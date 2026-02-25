import requests
from config import BLOCKCHAIN_API_URL, WALLET_ADDRESS

def get_wallet_data():
    """
    Fetch wallet data from blockchain API.
    Returns JSON response with wallet details.
    """
    url = f"{BLOCKCHAIN_API_URL}/addrs/{WALLET_ADDRESS}/full"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error: {response.status_code}")

def get_balance(wallet_data):
    """
    Extract wallet balance from API response.
    Returns balance in BTC.
    """
    satoshis = wallet_data.get("final_balance", 0)
    return satoshis / 100000000  # Convert satoshi to BTC

def get_transactions(wallet_data):
    """
    Extract transactions list from wallet data.
    """
    return wallet_data.get("txs", [])
