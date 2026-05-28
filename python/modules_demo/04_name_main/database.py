# database.py - Module file demonstrating __name__ behavior
def connect():
    print("Successfully connected to Database.")

# If someone runs "python database.py" directly, let's run diagnostics
if __name__ == "__main__":
    print(f"--- __name__ is '{__name__}' (Direct Run) ---")
    print("Running internal diagnostics tests for database.py...")
    connect()
    print("All diagnostics checks passed!")
else:
    print(f"--- database.py loaded as module. __name__ is '{__name__}' ---")
