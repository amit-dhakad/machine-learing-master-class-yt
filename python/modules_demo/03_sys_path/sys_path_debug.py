# sys_path_debug.py - Inspecting and editing the search directories
import sys

print("--- Current Python Search Directories (sys.path) ---")
for idx, path in enumerate(sys.path):
    print(f"[{idx}] {path}")

# In an actual script, you could dynamically append paths:
# sys.path.append("D:/my_custom_code_folder")
# print("\nAdded a custom path to sys.path.")
