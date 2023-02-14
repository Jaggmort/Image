import telegram
import os
import random
import time
import send_photo
from dotenv import load_dotenv


def main():
    load_dotenv()
    sleep_timer = os.environ.get('SLEEP_TIMER')
    chat_id = os.environ.get('CHAT_ID')
    telegram_token = os.environ.get('TELEGRAM_TOKEN')    
    available_images = []
    while True:
        time.sleep(int(sleep_timer))
        if not available_images:
            available_images = send_photo.get_images()
        random_choice = random.choice(available_images)
        send_photo.send_photo(f'Images/{random_choice}', chat_id, telegram_token)
        available_images.remove(random_choice)


if __name__=='__main__':
    main()
