import os
import asyncio
import requests
from PIL import Image
from dotenv import load_dotenv
from kinopoisk_dev import KinopoiskDev
from io import BytesIO

load_dotenv()
KINO_TOKEN = os.getenv('KINO_TOKEN')

kp = KinopoiskDev(token=KINO_TOKEN)

def upload_image(item):
    image = []
    for i in item.poster:
        image.append(i[1])
    response = requests.get(image[1])
    image_data = response.content
    image_poster = Image.open(BytesIO(image_data))
    return image_poster



item = asyncio.run(kp.arandom())
date_movie = {
    'name': item.name,
    'year': item.year,
    'description': item.description,
    'poster': upload_image(item),
    }



