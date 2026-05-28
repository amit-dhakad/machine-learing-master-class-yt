# app.py - Main application script importing database
import database   # This will trigger database.py's else block, but NOT the diagnostics block!

print("\n[App] Application starting...")
database.connect()
