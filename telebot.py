import telegram
import os
import random
import time
import send_photo
from dotenv import load_dotenv


if __name__=='__main__':
    load_dotenv()
    sleep_timer = os.environ.get('SLEEP_TIMER')
    available_images = []
    while True:
        time.sleep(int(sleep_timer))
        if available_images == [] or available_images[0] == []:
            available_images = send_photo.get_images_list()
        random_choice = random.choice(available_images[0])
        send_photo.send_photo(f'Images/{random_choice}')
        available_images[0].remove(random_choice)
