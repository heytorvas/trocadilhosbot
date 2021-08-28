import json, random, logging
from telegram.ext import Updater, CommandHandler
from util import create_connection, get_data_yaml
from time import sleep

TOKEN = get_data_yaml('TOKEN')
logging.basicConfig(filename="bot.log", level=logging.INFO)

def start(update, context):
    """Send a message when the command /start is issued."""
    logging.info('command start')
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("INSERT OR IGNORE INTO user(id,first_name,last_name,username) VALUES (?,?,?,?);", 
            (chat_id, first_name, last_name, username))
    con.commit()
    cursor.close()
    update.message.reply_text('Olá! Seja bem-vindo ao Trocadilhos Bot!')

def jokes(update, context):
    """Send a message when the command /trocadilho is issued."""
    logging.info('command trocadilho')
    with open("jokes.json", "r") as f:
        jokes = json.load(f)
    f.close()
    joke = random.choice(jokes)
    update.message.reply_text(joke['question'])
    sleep(0.5)
    update.message.reply_text(joke['answer'])

def main():
    """Start the bot."""
    logging.info('bot on')
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("trocadilho", jokes))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


main()