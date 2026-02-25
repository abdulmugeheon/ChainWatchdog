from config import ALERT_THRESHOLD

def check_large_transactions(transactions):
    """
    Check transactions exceeding the alert threshold.
    Returns list of suspicious transactions.
    """
    flagged = []

    for tx in transactions:
        for output in tx.get("outputs", []):
            value_btc = output.get("value", 0) / 100000000
            
            # Trigger alert if transaction value exceeds threshold
            if value_btc >= ALERT_THRESHOLD:
                flagged.append({
                    "tx_hash": tx.get("hash"),
                    "amount": value_btc
                })

    return flagged
