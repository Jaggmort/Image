import telegram
import os
import random
import time
from dotenv import load_dotenv


if __name__=='__main__':
    load_dotenv()
    sleep_timer = os.environ.get('SLEEP_TIMER')    
    while True:
        time.sleep(sleep_timer)
        bot = telegram.Bot(token='6249525717:AAEgl00yHNRKsuTiqiLIdNHYC6ZREzlqrJc')
        images_list = (os.walk('Images'))
        img = []
        for i in images_list:
            img.append(i[2])
        bot.send_document(chat_id=-1001836409919, document=open(f'Images/{random.choice(img[0])}', 'rb'))