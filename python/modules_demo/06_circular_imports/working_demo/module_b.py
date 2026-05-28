# module_b.py - Circular Import Solved (Deferred Import)

def action_b():
    print("Action B executed successfully!")

def trigger_a():
    print("Triggering Action A...")
    # DEFERRED LOCAL IMPORT: Loaded only when function is executed
    import module_a
    module_a.action_a()
