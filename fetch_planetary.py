import os
import requests
import common_utils
import argparse
from dotenv import load_dotenv
from datetime import datetime


def main():
    parser=argparse.ArgumentParser(description='Получает изображения запуска spacex по id')
    parser.add_argument('--start', help='Дата начала выборки',default=f"{datetime.today().strftime('%Y-%m-%d')}")
    args=parser.parse_args()    
    load_dotenv()
    nasa_api_key = os.environ.get('NASA_API_KEY')
    params = {'api_key':nasa_api_key, 'start_date':f'{args.start}'}
    common_utils.create_directory('Images')
    fetch_planetary(params)

def fetch_planetary(params):
    response = requests.get('https://api.nasa.gov/planetary/apod',params=params) 
    response.raise_for_status()
    image_links = response.json()
    for index_number, image_link in enumerate(image_links):
        prepared_url =  f"Images/planetary_{index_number}{common_utils.get_extension(image_link['url'])}"
        common_utils.get_image(image_link['url'], prepared_url) 
    return

if __name__=='__main__':
    main()