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
    telegram_token = os.environ.get('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=telegram_token)
    bot.send_document(chat_id=-1001836409919, document=open(Image, 'rb'))



if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Получает изображения запуска spacex по id')
    parser.add_argument('--Image', help='Имя файла для отправки',default=f'{random.choice(get_images()[0])}')
    args=parser.parse_args()   
    send_photo(f'Images/{args.Image}')