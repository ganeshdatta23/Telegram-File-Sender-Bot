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

## How to Create a Telegram Bot and Get Bot Token and Chat ID

### Step 1: Create a Telegram Bot

1. **Open Telegram:**
   - Download and install Telegram on your device (if not already installed).
   - Log in to your account.

2. **Search for BotFather:**
   - In the search bar, type `BotFather` and select the verified account (with a blue checkmark).

3. **Start the BotFather:**
   - Click the **Start** button or send the `/start` command.

4. **Create a New Bot:**
   - Send the `/newbot` command to BotFather.
   - Follow the prompts:
     - Enter a name for your bot (e.g., `My File Sender Bot`).
     - Choose a unique username for your bot (it must end with `bot`, e.g., `FileSenderBot`).

5. **Get the Bot Token:**
   - Once the bot is created, BotFather will send you a message containing the bot token.
     - Example: `123456789:ABCDEFghijklmnopqrstuvwxyz123456789`.
   - **Save this token** securely, as it is required for your bot to communicate with the Telegram API.

### Step 2: Add Your Bot to a Group

1. **Search for Your Bot:**
   - In Telegram, search for your bot using the username you set (e.g., `@FileSenderBot`).

2. **Start Your Bot:**
   - Open the chat with your bot and click **Start**.

3. **Create a Group:**
   - Create a new group chat or open an existing one.

4. **Add the Bot to the Group:**
   - Add your bot to the group as a member.
   - Promote the bot as an **admin** if needed (e.g., if the bot requires permissions to send messages).

### Step 3: Get the Chat ID

#### Method 1: Using the Telegram Bot

1. **Send a Message** in the group where the bot is added.
2. **Use a Bot API Request:**
   - Open your web browser and paste the following URL, replacing `<BOT_TOKEN>` with your bot token:
     ```plaintext
     https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
     ```
   - Example: `https://api.telegram.org/bot123456789:ABCDEFghijklmnopqrstuvwxyz123456789/getUpdates`.

3. **Check the Response:**
   - The response will contain recent messages sent to your bot. Look for the `chat` section:
     ```json
     {
       "update_id": 123456789,
       "message": {
         "chat": {
           "id": -987654321,
           "title": "My Group",
           "type": "group"
         },
         "text": "Hello"
       }
     }
     ```
   - The `id` under `chat` is the **chat ID** (e.g., `-987654321` for a group or a positive number for a private chat).

#### Method 2: Using Third-Party Bots

1. **Add the Bot to the Group:**
   - Search for a bot like `@userinfobot` or `@getidsbot` on Telegram.
   - Add it to the group where you added your bot.

2. **Send a Command:**
   - Use commands like `/start` or `/get_id`.
   - The bot will respond with the chat ID.

## Notes

- Ensure your Telegram bot has the required permissions to send files in the group.
- Be cautious with large folders, as Telegram's API has file size limits.
- Handle sensitive information like the bot token securely.
