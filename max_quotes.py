import os
from datetime import datetime

# Path to the file to modify
file_path = "example.txt"

def modify_file():
    """Appends the current timestamp to the file."""
    with open(file_path, "a") as f:
        f.write(f"Update made at {datetime.now()}\n")
    print(f"Modified {file_path} successfully.")

if __name__ == "__main__":
    # Check if the file exists, if not create it
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("Initial content for example.txt\n")
    modify_file()
