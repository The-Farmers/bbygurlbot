from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import random
import time
import os
PORT = int(os.environ.get('PORT', 5000))
TOKEN = "5034249047:AAG-gTC5BeIoUDYyg21VoFoYZn9hZKRlCXI"
IDONTCARE = range(1)

def start(update, context):
    feels = [['Great! Thanks for asking <3', 'I don\'t feel so good Mr. Stark']]
    startmsg = """
    Wassup I\'m ur bbygurl ★~(◠ω◕✿)
    How are you feeling today?
    """
    update.message.reply_text(
        startmsg,
        reply_markup=ReplyKeyboardMarkup(feels, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Your feelz'),
    )
    return IDONTCARE

def idontcare(update, context):
    dontcaremsg = """
    Jk I don\'t rly care.
    So wdya want? ^^\n
    /Bro - I\'m in cs, I need a life.
    /Help - I\'m in cs, I need a job.
    /Me - I\'m in cs, can I get a date?
    /Please - I\'m in cs, can you say smth nice?
    """
    update.message.reply_text(dontcaremsg)
    return ConversationHandler.END

gifs =['https://media1.tenor.com/images/641401eee7aa708660ed39233b13b736/tenor.gif?itemid=5809496',
'https://c.tenor.com/PpNvpoh9b-sAAAAC/lee-minho-disgusting-shit.gif', 'https://c.tenor.com/Xcr8fHyf84gAAAAC/baka-anime.gif']

def bro(update, context):
    context.bot.send_document(chat_id=update.effective_chat.id, document=gifs[0])

def mcd(update, context):
    update.message.reply_text('Good luck!!!')
    update.message.reply_text('https://www.mcdonalds.com.sg/careers/roles/crew/')

def me(update, context):
    context.bot.send_document(chat_id=update.effective_chat.id, document=gifs[1])

def please(update, context):
    update.message.reply_text('U poor kid :(')
    time.sleep(1.5)
    update.message.reply_text('Sikeee')
    context.bot.send_document(chat_id=update.effective_chat.id, document=gifs[2])

def insult(update, context):
    context.bot.send_document(chat_id=update.effective_chat.id, document=gifs[random.randrange(3)])

def nani(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Nani??")

def main():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            IDONTCARE: [MessageHandler(Filters.text, idontcare)],
        },
        fallbacks=[],
    )

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("Bro", bro))
    dispatcher.add_handler(CommandHandler("Help", mcd))
    dispatcher.add_handler(CommandHandler("Me", me))
    dispatcher.add_handler(CommandHandler("Please", please))
    dispatcher.add_handler(CommandHandler("insult", insult))
    dispatcher.add_handler(MessageHandler(Filters.text | Filters.command, nani))

    updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
    updater.bot.setWebhook('https://damp-lake-67169.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()