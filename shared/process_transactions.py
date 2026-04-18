import csv
import random
from datetime import datetime

def process_transactions():
    transactions = []
    for i in range(20):
        transactions.append({
            "id": i + 1,
            "amount": round(random.uniform(10, 5000), 2),
            "currency": random.choice(["USD", "EUR", "EGP", "GBP"]),
            "category": random.choice(["food", "travel", "bills", "shopping"]),
            "status": random.choice(["approved", "declined", "pending"]),
            "timestamp": datetime.now().isoformat()
        })

    filepath = "/opt/airflow/shared/transaction_report.csv"
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=transactions[0].keys())
        writer.writeheader()
        writer.writerows(transactions)

    print(f"[✓] Report saved to {filepath}")
    return filepath

if __name__ == "__main__":
    process_transactions()
