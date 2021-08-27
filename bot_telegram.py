import yaml, requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from util import create_connection

with open('env.yaml', 'r') as f:
    TOKEN = yaml.safe_load(f)['TOKEN']

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Olá! Seja bem-vindo ao Trocadilhos Bot!')
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates').json()
    con = create_connection()
    for i in response['result']:
        user = i['message']['from']
        
        cursor = con.cursor()
        cursor.execute("INSERT OR IGNORE INTO user(id,is_bot,first_name,last_name,username,language_code) VALUES (?,?,?,?,?,?);", 
                (user['id'], user['is_bot'], 
                user['first_name'], user['last_name'], 
                user['username'], user['language_code']))
        con.commit()
        cursor.close()

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    #logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


main()