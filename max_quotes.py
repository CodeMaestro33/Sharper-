import os
import subprocess
from datetime import datetime
import random

# File to modify
file_path = "changes.txt"

# Generate some content
new_content = f"Change made at {datetime.now()}. Random number: {random.randint(1, 100)}\n"

# Append the content to the file
with open(file_path, "a") as file:
    file.write(new_content)

# Automate Git operations
try:
    # Configure Git (use your GitHub username and email)
    subprocess.run(["git", "config", "user.name", "your-username"], check=True)
    subprocess.run(["git", "config", "user.email", "your-email@example.com"], check=True)

    # Stage changes
    subprocess.run(["git", "add", file_path], check=True)

    # Commit changes
    commit_message = f"Auto-update at {datetime.now()}"
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Push changes to the repository
    subprocess.run(["git", "push"], check=True)

    print("Changes pushed successfully!")

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
