import os
import random
import telegram
import argparse
from dotenv import load_dotenv

def get_images():
    images = (os.walk('Images'))
    available_images = []
    for image in images:
        available_images.append(image[2])
    return available_images

def send_photo(Image):
    load_dotenv()
    chat_id = os.environ.get('CHAT_ID')
    telegram_token = os.environ.get('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=telegram_token)
    with open (Image, 'rb') as document:
        bot.send_document(chat_id=chat_id, document=document)



if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Получает изображения запуска spacex по id')
    parser.add_argument('--Image', help='Имя файла для отправки',default=f'{random.choice(get_images()[0])}')
    args=parser.parse_args()   
    send_photo(f'Images/{args.Image}')