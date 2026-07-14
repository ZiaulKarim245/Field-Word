CUSTOMERS = {
    "priya@example.com": {
        'customer_id': 'C-1001',
        'name': 'Priya Nair',
        'plan': 'Pro',
        'status': 'active',
        'since': '2023-02-11'
    },
    "ziaul245@gmail.com": {
        'customer_id': 'C-1002',
        'name': 'Ziaul Karim',
        'plan': 'Pro',
        'status': 'active',
        'since': '2026-07-14'
    }
}

INVOICES = {
    "INV-5013": {
        "customer_id": "C-1001",
        "month": "January",
        "amount": 49.00,
        "status": "Paid"
    },
    "INV-5014": {
        "customer_id": "C-1002",
        "month": "February",
        "amount": 49.00,
        "status": "Paid"
    }
}

REFUNDS = {
    "INV-5013": {
        "status": "Processed",
        "invoice_id": "INV-5013",
        "amount": 49.00,
        "eta": "Completed"
    }
}
