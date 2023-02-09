import requests
import os
import pathlib
from pathlib import Path
from urllib.parse import urlparse


def get_image(url, filename):   
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)
    return

def fetch_spacex_last_launch():
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images',params=params) 
    epic_links = response.json()
    for epic_link in epic_links:
        date = epic_link['date']
        image = epic_link['image']
        image_png = f'images/{image}.png'
        get_image(f'https://api.nasa.gov/EPIC/archive/natural/{date[0:4]}/{date[5:7]}/{date[8:10]}/png/{image}.png',image_png )
    return

if __name__=='__main__':
    params={'api_key':'t0z6pl2FRadcRh17Pu4mRXDJklSgQpYhS9me7zvG'}    
    current_directory=f'{pathlib.Path().resolve()}\images'
    Path(current_directory).mkdir(parents=True, exist_ok=True)    
    fetch_spacex_last_launch()