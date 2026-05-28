# ecommerce/payments.py - Sub-module of ecommerce package
# Relative import from sibling file: shipping.py
from .shipping import deliver

def process_upi(amount):
    print(f"Payments: Processing UPI payment of Rs. {amount}")
    # Call the sibling module function
    deliver()
