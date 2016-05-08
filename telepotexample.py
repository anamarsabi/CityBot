import telepot
bot = telepot.Bot('217137800:AAFNSkLiiYeG9niWoXvgQlGA2IblipNYrsg')
from pprint import pprint
response = bot.getUpdates()
pprint(response)
def handle(msg):
pprint(msg)
bot.message_loop(handle)
bot.sendMessage('@learnitgirlCityBot', 'Good morning!')
