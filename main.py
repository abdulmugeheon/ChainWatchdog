from tracker import get_wallet_data, get_balance, get_transactions
from alerts import check_large_transactions

def main():
    """
    Main entry point of BlockSentinel.
    Fetches wallet data, prints balance,
    and checks for suspicious transactions.
    """
    print("🔍 BlockSentinel is monitoring wallet...\n")

    wallet_data = get_wallet_data()
    balance = get_balance(wallet_data)
    transactions = get_transactions(wallet_data)

    print(f"Current Balance: {balance} BTC")
    print(f"Total Transactions: {len(transactions)}")

    flagged = check_large_transactions(transactions)

    if flagged:
        print("\n🚨 Suspicious Transactions Detected:")
        for tx in flagged:
            print(f"- TX: {tx['tx_hash']} | Amount: {tx['amount']} BTC")
    else:
        print("\n✅ No suspicious transactions found.")

if __name__ == "__main__":
    main()
