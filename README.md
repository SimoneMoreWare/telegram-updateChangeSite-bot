<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Telegram Page Change Monitor Bot</title>
</head>
<body>
    <h1>Telegram Page Change Monitor Bot</h1>
    <p>This bot monitors a specified webpage for changes and sends notifications via Telegram.</p>

    <h2>Features</h2>
    <ul>
        <li>Checks the specified webpage for content changes.</li>
        <li>Sends a Telegram message when the content changes.</li>
    </ul>

    <h2>Requirements</h2>
    <p>To run this bot, you need the following:</p>
    <ul>
        <li>Python 3.x</li>
        <li><code>requests</code></li>
        <li><code>beautifulsoup4</code></li>
        <li><code>python-telegram-bot</code></li>
    </ul>
    <p>You can install the required libraries using pip:</p>
    <pre><code>pip install requests beautifulsoup4 python-telegram-bot</code></pre>

    <h2>How to Create a Telegram Bot</h2>
    <ol>
        <li><strong>Open Telegram</strong>: Launch the Telegram app on your device.</li>
        <li><strong>Search for BotFather</strong>: In the search bar, type <code>@BotFather</code> and select the official BotFather bot.</li>
        <li><strong>Create a New Bot</strong>:
            <ul>
                <li>Type <code>/newbot</code> and follow the prompts to set a name and username for your bot.</li>
                <li>Once created, BotFather will give you a token. Save this token; you will need it for your script.</li>
            </ul>
        </li>
        <li><strong>Add Your Bot to a Chat</strong>: You can add your bot to a group chat or send messages directly to it.</li>
    </ol>

    <h2>How to Get Your Chat ID</h2>
    <ol>
        <li><strong>Start a Chat with Your Bot</strong>: Send a message to your bot in Telegram.</li>
        <li><strong>Get the Chat ID</strong>:
            <ul>
                <li>Open your web browser and navigate to the following URL, replacing <code>YOUR_BOT_TOKEN</code> with your bot's token: 
                    <pre><code>https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates</code></pre>
                </li>
                <li>Look for the <code>chat</code> object in the response. The <code>id</code> field inside this object is your chat ID.</li>
            </ul>
        </li>
    </ol>

    <h2>Code Explanation</h2>
    <p>The code uses the <code>requests</code> library to fetch webpage content.</p>
    <p>The <code>BeautifulSoup</code> library is used for parsing HTML.</p>
    <p>The bot sends notifications using the <code>python-telegram-bot</code> library.</p>

    <h2>Running the Bot</h2>
    <ol>
        <li>Replace <code>YOUR_BOT_TOKEN</code> and <code>YOUR_CHAT_ID</code> in the script with your bot token and chat ID.</li>
        <li>Run the script using Python:
            <pre><code>python bot.py</code></pre>
        </li>
    </ol>

    <h2>Further Reading</h2>
    <ul>
        <li><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup Documentation</a></li>
        <li><a href="https://docs.python-requests.org/en/master/">Requests Documentation</a></li>
        <li><a href="https://docs.python.org/3/library/asyncio.html">Python Asyncio Documentation</a></li>
    </ul>

    <h2>Contributing</h2>
    <p>Feel free to submit issues or pull requests.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
</body>
</html>
