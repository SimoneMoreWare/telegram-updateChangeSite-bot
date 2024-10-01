# telegram-updateChangeSite-bot
This bot monitors a specified webpage for changes and sends notifications via Telegram.

# Features
--------

*   Checks the specified webpage for content changes.
*   Sends a Telegram message when the content changes.

# Requirements
------------

To run this bot, you need the following:

*   Python 3.x
*   `requests`
*   `beautifulsoup4`
*   `python-telegram-bot`

You can install the required libraries using pip:

    pip install requests beautifulsoup4 python-telegram-bot

# How to Create a Telegram Bot
----------------------------

1.  **Open Telegram**: Launch the Telegram app on your device.
2.  **Search for BotFather**: In the search bar, type `@BotFather` and select the official BotFather bot.
3.  **Create a New Bot**:
    *   Type `/newbot` and follow the prompts to set a name and username for your bot.
    *   Once created, BotFather will give you a token. Save this token; you will need it for your script.
4.  **Add Your Bot to a Chat**: You can add your bot to a group chat or send messages directly to it.

How to Get Your Chat ID
-----------------------

1.  **Start a Chat with Your Bot**: Send a message to your bot in Telegram.
2.  **Get the Chat ID**:
    *   Open your web browser and navigate to the following URL, replacing `YOUR_BOT_TOKEN` with your bot's token:
        
            https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
        
    *   Look for the `chat` object in the response. The `id` field inside this object is your chat ID.

# Code Explanation
----------------

The code uses the `requests` library to fetch webpage content.

The `BeautifulSoup` library is used for parsing HTML.

The bot sends notifications using the `python-telegram-bot` library.

# Running the Bot
---------------

1.  Replace `YOUR_BOT_TOKEN` and `YOUR_CHAT_ID` in the script with your bot token and chat ID.
2.  Run the script using Python:
    
        python bot.py
    

Further Reading
---------------

*   [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
*   [Requests Documentation](https://docs.python-requests.org/en/master/)
*   [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

Contributing
------------

Feel free to submit issues or pull requests.

License
-------

This project is licensed under the MIT License.
