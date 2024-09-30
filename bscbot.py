import telebot
from web3 import Web3

# Set up your bot with the actual token from BotFather
BOT_TOKEN = "7312574044:AAHPwChJdj_iJVPMLCweggM2ejEj_vs9D8E"  # Replace this with your token
bot = telebot.TeleBot(BOT_TOKEN)

# Connect to BEP20 testnet
bsc_testnet = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(bsc_testnet))

# Metamask address
metamask_address = "0xBfD0ce152E03DdEd694100099559F21EF137091d"

# Affiliate program
affiliate_level = {}

# Game data
user_data = {}
rewards_per_tap = 1  # Number of tokens per tap


# Start command
@bot.message_handler(commands=['start'])
def start_game(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Welcome to Tap to Earn game!\nConnect your Metamask wallet to start playing.")

    # Placeholder for metamask connection
    bot.send_message(chat_id, "Click here to connect Metamask: [Metamask Connect URL]")

    # Store user data
    user_data[chat_id] = {'taps': 0, 'wallet_connected': False}


# Handle wallet connection (Simulated)
@bot.message_handler(commands=['connect_wallet'])
def connect_wallet(message):
    chat_id = message.chat.id
    if web3.isConnected():
        # Simulate wallet connection
        user_data[chat_id]['wallet_connected'] = True
        bot.send_message(chat_id, "Metamask wallet connected successfully!")
    else:
        bot.send_message(chat_id, "Failed to connect wallet. Please try again.")


# Tap button
@bot.message_handler(commands=['tap'])
def tap_to_earn(message):
    chat_id = message.chat.id
    if user_data[chat_id]['wallet_connected']:
        user_data[chat_id]['taps'] += 1
        bot.send_message(chat_id, f"You tapped! Total taps: {user_data[chat_id]['taps']}")

        # Reward user with tokens
        bot.send_message(chat_id, f"You earned {rewards_per_tap} tokens!")
    else:
        bot.send_message(chat_id, "Please connect your wallet first using /connect_wallet.")


# Affiliate system
@bot.message_handler(commands=['affiliate'])
def affiliate_link(message):
    chat_id = message.chat.id
    affiliate_link = f"https://t.me/{bot.get_me().username}?start={chat_id}"
    affiliate_level[chat_id] = 0
    bot.send_message(chat_id, f"Share your affiliate link: {affiliate_link}")
    bot.send_message(chat_id, "For each friend you refer, you earn bonus tokens!")


bot.polling()
