# -*- coding: utf-8 -*-
import random
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis

#       Your bot code below
# bot = telebot.TeleBot(token)
bot = telebot.TeleBot(TOKEN)
# some_api = some_api_lib.connect(some_api_token)
def select_response(message):
	responses = ['Ie {} tio, no et canses?', '{}, eres un puto pesat de tio', 'Ie {}, ja hi ha prou que ja cansa',
				'Collons {}, que pesat eres quan vols', "Que si {}, tio pesat, que ja t'hem llegit"]

	response_to_use = random.choice(responses)
	name = unicodedata.normalize('NFKD', message.from_user.first_name).encode('ascii','ignore')
	response = response_to_use.format(name)

	return response


# The decorator (@bot.message_handler) indicates the type of messages that will activate this function
# In this case, we'll activate it for every message. See telebot API for more possibilities 
@bot.message_handler(func=lambda message: True)
def pole_reply(message):
	# If the message contains the word 'pole' (case insensitive), the bot replies
	if 'pole' in message.text.lower():
		resposta = select_response(message)
		bot.reply_to(message, resposta)
#              ...
