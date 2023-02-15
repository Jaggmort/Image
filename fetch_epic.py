import os
import requests
import common_utils
from dotenv import load_dotenv 
from urllib.parse import urlparse


def main():
    load_dotenv()
    params = {'api_key':f"{os.environ.get('NASA_API_KEY')}"}
    common_utils.create_directory('Images')
    fetch_epic(params)

def fetch_epic(params):
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images',params=params) 
    response.raise_for_status()
    epic_links = response.json()
    for epic_link in epic_links:
        date = epic_link['date']
        image = epic_link['image']
        image_png = f'images/{image}.png'
        prepared_url = f'https://api.nasa.gov/EPIC/archive/natural/{date[0:4]}/{date[5:7]}/{date[8:10]}/png/{image}.png'
        common_utils.get_image(prepared_url,image_png, params)
    return

if __name__=='__main__':
    main()