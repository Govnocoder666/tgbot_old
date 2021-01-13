from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler

button_test = 'Click'

def message_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text = button_test),
			],
		],

		resize_keyboard = True,
	)

	update.message.reply_text(
		text = "Press the button, pls",
		reply_markup = reply_markup,
	)

def main():
	print('Start')

	updater = Updater(
		token = '1550742706:AAHGxUhxlokRVAZcOUWI-pWS5iMseqWBCdE',
		use_context = True,
	)

	updater.dispatcher.add_handler(MessageHandler(filters = Filters.all, callback = message_handler))
	updater.start_polling()
	updater.idle()	

if __name__ == '__main__':
		main()	