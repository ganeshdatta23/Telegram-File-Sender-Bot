```python
# Telegram File Sender Script

"""
This script automates the process of sending files from a local folder to a Telegram group chat.
It traverses the folder, uploads files using the Telegram Bot API, and deletes them after a successful upload.
"""

import os
import requests

# Replace with your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Replace with your group chat ID
CHAT_ID = "YOUR_CHAT_ID"

# Path to the folder containing the files
folder_path = r"YOUR_FOLDER_PATH"

def send_file(file_path):
    """Send a file to the Telegram group."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as file:
        response = requests.post(
            url,
            data={"chat_id": CHAT_ID},
            files={"document": file}
        )
    return response.json()

if __name__ == "__main__":
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                print(f"Sending: {file_path}")
                result = send_file(file_path)
                if result.get("ok"):
                    print(f"Sent: {file_path}")
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                else:
                    print(f"Failed to send: {file_path}. Error: {result}")
            except Exception as e:
                print(f"Error sending {file_path}: {e}")
```
