# main.py - Demonstrates importing packages and sub-modules
import ecommerce             # Triggers execution of ecommerce/__init__.py
from ecommerce import payments  # Import payments sub-module

print("\n--- Package Demo Running ---")
print("Version:", ecommerce.VERSION)
payments.process_upi(499)
