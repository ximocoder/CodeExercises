# telegram bot
# para autocontestar a ciertos usuarios
# ximo

from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler

def start(bot, update):
    update.message.reply_text('Hello World!')

def angel(bot, update):
    if update.message.from_user.username == "AngeluKing":
        update.message.reply_text('Angel Luis eres un hijo de puta!')
    else:
        update.message.reply_text('Angel Luis? ese es un hijo de puta')
def javi(bot, update):
    if update.message.from_user.username == "AngeluKing":
        update.message.reply_text('Angel hijo de puta!')
    else:
        update.message.reply_text('Jaaaaaaaaaaaaaaaaaaaavi!')
        update.message.reply_text('ven ratita, asoma la colita...')

def hello(bot, update):
    if update.message.from_user.username == "AngeluKing":
        update.message.reply_text('Angel hijo de puta!')
    else:
        update.message.reply_text(
            'Hola {}'.format(update.message.from_user.first_name))
def contesta(bot, update):
    if update.message.from_user.username == "AngeluKing":
        update.message.reply_text('Hijo de puta!')
    if update.message.from_user.username == "":
        update.message.reply_text('Ximo, eres el más grande!')

def contesta2(bot, update):
    if update.message.from_user.username == "AngeluKing":
        update.message.reply_text('Hijo de puta!')
    if update.message.from_user.username == "":
        update.message.reply_text('Ximo, eres el más grande!')

updater = Updater('')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('javi', javi))
updater.dispatcher.add_handler(CommandHandler('angel', angel))
updater.dispatcher.add_handler(MessageHandler(Filters.all, contesta))
updater.dispatcher.add_handler(MessageHandler(Filters.text, contesta))

#updater.dispatcher.add_handler(ConversationHandler(Filters.all, contesta2))



updater.start_polling()
updater.idle()