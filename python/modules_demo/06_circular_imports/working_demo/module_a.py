# module_a.py - Circular Import Solved (Deferred Import)

def action_a():
    print("Action A executed successfully!")

def trigger_b():
    print("Triggering Action B...")
    # DEFERRED LOCAL IMPORT: Loaded only when function is executed, 
    # after both modules have finished initial compile/load time.
    import module_b
    module_b.action_b()
