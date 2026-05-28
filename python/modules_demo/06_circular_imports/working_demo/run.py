# run.py - Execute solved circular import
print("--- Starting solved circular import test (Local Imports) ---")

import module_a
# Both modules compile successfully without recursion deadlock!
module_a.trigger_b()

print("\n--- Triggering reverse path ---")
import module_b
module_b.trigger_a()

print("\nSuccess! Deadlock resolved.")
