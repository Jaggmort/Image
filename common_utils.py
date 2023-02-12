import os
import requests
import pathlib
from pathlib import Path
from urllib.parse import urlparse


def get_image(url, filename, params=''):   
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
    return

def create_directory(directory):
    current_directory=f'{pathlib.Path().resolve()}\{directory}'
    Path(current_directory).mkdir(parents=True, exist_ok=True)  

def get_extension(url):
    parse = urlparse(url)
    extension = os.path.splitext(parse.path)
    return extension[1]    