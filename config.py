import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API endpoint for blockchain data (example: BlockCypher API)
BLOCKCHAIN_API_URL = "https://api.blockcypher.com/v1/btc/main"

# Wallet address to monitor
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

# Alert threshold in BTC
ALERT_THRESHOLD = float(os.getenv("ALERT_THRESHOLD", 0.1))
