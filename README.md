# Telegram File Sender

This repository contains a Python script to send files from a local folder to a specified Telegram group chat using the Telegram Bot API.

## Features

- Automatically scans a folder and its subfolders for files.
- Sends files to a Telegram group chat using a bot.
- Deletes files after successful upload.

## Requirements

- Python 3.x
- A Telegram bot token.
- Chat ID of the Telegram group.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/telegram-file-sender.git
   cd telegram-file-sender
   ```

2. **Install dependencies:**

   This script uses the `requests` library, which can be installed using:

   ```bash
   pip install requests
   ```

3. **Configure the script:**

   - Replace `BOT_TOKEN` with your Telegram bot token.
   - Replace `CHAT_ID` with the chat ID of the group.
   - Replace `folder_path` with the path to the folder containing the files.

## Usage

1. **Run the script:**

   Execute the Python script:

   ```bash
   python send_files_to_telegram.py
   ```

2. **Watch the progress:**

   - The script will log the files being sent.
   - Files will be deleted from the local folder after successful upload.

## Script Explanation

Here is a breakdown of the main sections of the script:

### Imports

```python
import os
import requests
```

- `os`: Used to traverse the folder structure and manage files.
- `requests`: Used to interact with the Telegram Bot API.

### Configuration

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = YOUR_CHAT_ID
folder_path = r"YOUR_FOLDER_PATH"
```

- Replace placeholders with your actual bot token, chat ID, and folder path.

### File Sending Function

```python
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
```

- This function sends a file to the Telegram group and returns the API response.

### File Traversal and Sending

```python
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

- Traverses the specified folder and sends each file to the Telegram group.
- Deletes files after successful upload to save space.# Telegram File Sender

This repository contains a Python script to send files from a local folder to a specified Telegram group chat using the Telegram Bot API.

## Features

- Automatically scans a folder and its subfolders for files.
- Sends files to a Telegram group chat using a bot.
- Deletes files after successful upload.

## Requirements

- Python 3.x
- A Telegram bot token.
- Chat ID of the Telegram group.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/telegram-file-sender.git
   cd telegram-file-sender
   ```

2. **Install dependencies:**

   This script uses the `requests` library, which can be installed using:

   ```bash
   pip install requests
   ```

3. **Configure the script:**

   - Replace `BOT_TOKEN` with your Telegram bot token.
   - Replace `CHAT_ID` with the chat ID of the group.
   - Replace `folder_path` with the path to the folder containing the files.

## Usage

1. **Run the script:**

   Execute the Python script:

   ```bash
   python send_files_to_telegram.py
   ```

2. **Watch the progress:**

   - The script will log the files being sent.
   - Files will be deleted from the local folder after successful upload.

## Script Explanation

Here is a breakdown of the main sections of the script:

### Imports

```python
import os
import requests
```

- `os`: Used to traverse the folder structure and manage files.
- `requests`: Used to interact with the Telegram Bot API.

### Configuration

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = YOUR_CHAT_ID
folder_path = r"YOUR_FOLDER_PATH"
```

- Replace placeholders with your actual bot token, chat ID, and folder path.

### File Sending Function

```python
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
```

- This function sends a file to the Telegram group and returns the API response.

### File Traversal and Sending

```python
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

- Traverses the specified folder and sends each file to the Telegram group.
- Deletes files after successful upload to save space.
