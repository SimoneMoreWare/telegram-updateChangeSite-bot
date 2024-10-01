import requests
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio

# Global Variables
bot_token = 'YOUR_BOT_TOKEN'  # Replace with your bot token
chat_id = 'YOUR_CHAT_ID'  # Replace with your chat ID
url = 'URL_TO_MONITOR'  # Replace with the URL you want to monitor
REQUEST_TIMEOUT = 10  # Timeout for the request in seconds
SLEEP_DURATION = 3600  # Sleep duration between checks in seconds (1 hour)

# Function to check if the page content has changed
def check_for_updates():
    try:
        # Make a GET request to the specified URL
        response = requests.get(url, timeout=REQUEST_TIMEOUT)  # Use global timeout
        if response.status_code == 200:
            # If the request is successful, parse the content
            soup = BeautifulSoup(response.content, 'html.parser')
            new_content = soup.text.strip()  # Get the page content as text
            return new_content
        else:
            # Handle unexpected status codes
            return None
    except requests.RequestException as e:
        # Handle any request exceptions
        return None

# Main asynchronous function
async def main():
    # Initialize the Telegram bot
    bot = Bot(token=bot_token)

    # Store the initial content of the page
    old_content = check_for_updates()

    # Periodically check for updates
    while True:
        new_content = check_for_updates()
        
        if new_content is not None:
            if new_content != old_content:
                # If content has changed, send a message to the Telegram chat
                await bot.send_message(chat_id=chat_id, text="The monitored page has been updated!")
                old_content = new_content  # Update stored content
        await asyncio.sleep(SLEEP_DURATION)  # Use global sleep duration

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
