# run.py - Execute failing circular import
print("--- Starting failing circular import test ---")
try:
    import module_a
    module_a.trigger_b()
except Exception as e:
    import traceback
    print("\n--- CIRCULAR IMPORT DEADLOCK DETECTED! ---")
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Message: {e}")
    print("\nTraceback:")
    traceback.print_exc()
