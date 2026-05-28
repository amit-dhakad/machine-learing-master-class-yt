# module_b.py - Circular Import Error (Failing)
from module_a import action_a

def action_b():
    print("Action B executed!")

def trigger_a():
    print("Triggering Action A...")
    action_a()
