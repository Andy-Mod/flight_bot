from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from chat import get_response, predict_class
from train import train 

updater = Updater("5220119712:AAFWIyM9D7WYzMoUIXcA0koYNTl9PXtpRsQ",
				use_context=True)

def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Salutation brave internaute. \n\
  	Merçi d'avoir adhérer à notre service. Pour plus d'information tapez la commande /help.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/service - Pour contacter le service client.
 	/reservation - Pour procéder à la réservation d'un billet d'avion""")


def service_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Veillez formuler votre demande à l'adresse suivante :\
		flight.service@gmail.com)")

def reservation_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Réservation du billet d'avion.")

def discuss_text(update: Update, context: CallbackContext):
    tag = predict_class(update.message.text)
    response = get_response(tag)
    
    update.message.reply_text(response)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('reservation', reservation_url))
updater.dispatcher.add_handler(CommandHandler('service', service_url))
#updater.dispatcher.add_handler(MessageHandler(Filters.text, discuss))
#updater.dispatcher.add_handler(MessageHandler(
#	Filters.command, discuss)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, discuss_text))

updater.start_polling()
