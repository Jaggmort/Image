import os
import requests
import common_utils
import argparse
from dotenv import load_dotenv 
from urllib.parse import urlparse


def main():
    parser=argparse.ArgumentParser(description='Получает изображения запуска spacex по id')
    parser.add_argument('--id', help='id запуска', default='latest')
    args=parser.parse_args()
    common_utils.create_directory('Images')
    fetch_spacex_image(args.id)

def fetch_spacex_image(launch_number='latest'):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_number}')
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    for index_number, image_link in enumerate(image_links):
        common_utils.get_image(image_link, f'Images/spacex_{index_number}{common_utils.get_extension(image_link)}')
    return

if __name__=='__main__':
    main()
