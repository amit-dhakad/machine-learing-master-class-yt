# module_a.py - Circular Import Error (Failing)
from module_b import action_b

def action_a():
    print("Action A executed!")

def trigger_b():
    print("Triggering Action B...")
    action_b()
