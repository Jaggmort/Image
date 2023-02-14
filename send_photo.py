import os
import random
import telegram
import argparse
from dotenv import load_dotenv


def main():
    load_dotenv()
    chat_id = os.environ.get('CHAT_ID')
    telegram_token = os.environ.get('TELEGRAM_TOKEN')
    parser=argparse.ArgumentParser(description='Получает изображения запуска spacex по id')
    parser.add_argument('--Image', help='Имя файла для отправки',default=f'{random.choice(get_images()[0])}')
    args=parser.parse_args()   
    send_photo(f'Images/{args.Image}', chat_id=chat_id, telegram_token=telegram_token) 

def get_images():
    images = (os.walk('Images'))
    for image in images:
        __, __, available_images= image
    return available_images

def send_photo(Image, chat_id, telegram_token):
    bot = telegram.Bot(token=telegram_token)
    with open (Image, 'rb') as document:
        bot.send_document(chat_id=chat_id, document=document)



if __name__=='__main__':
    main()