import os
import asyncio
from PIL import Image
from dotenv import load_dotenv
from kinopoisk_dev import KinopoiskDev
import requests
from io import BytesIO

load_dotenv()
KINO_TOKEN = os.getenv('KINO_TOKEN')

kp = KinopoiskDev(token=KINO_TOKEN)
item = asyncio.run(kp.arandom())

'''Это тоже закрепить в функцию'''
print(item.name)
print(item.year)
print(item.description)



# """Это надо сделать в функцию"""
# image = []
# for i in item.poster:
#     image.append(i[1])
# response = requests.get(image[1])
# image_data = response.content
# image_poster = Image.open(BytesIO(image_data))
# image_poster.show()