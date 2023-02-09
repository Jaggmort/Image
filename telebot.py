import telegram

bot = telegram.Bot(token='6249525717:AAEgl00yHNRKsuTiqiLIdNHYC6ZREzlqrJc')
bot.send_document(chat_id=-1001836409919, document=open('Images/planetary_0.jpg', 'rb'))