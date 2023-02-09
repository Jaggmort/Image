import os
import requests
import common_utils
from dotenv import load_dotenv 
from urllib.parse import urlparse


def fetch_epic():
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images',params=params) 
    epic_links = response.json()
    for epic_link in epic_links:
        date = epic_link['date']
        image = epic_link['image']
        image_png = f'images/{image}.png'
        common_utils.get_image(f'https://api.nasa.gov/EPIC/archive/natural/{date[0:4]}/{date[5:7]}/{date[8:10]}/png/{image}.png',image_png, params)
    return

if __name__=='__main__':
    load_dotenv()
    NASA_API_KEY = os.environ.get('NASA_API_KEY')
    params = {'api_key':NASA_API_KEY}
    common_utils.create_directory('Images')
    fetch_epic()