import os
import requests
from PIL import Image
from dotenv import load_dotenv
from kinopoisk_dev import KinopoiskDev
from io import BytesIO

load_dotenv()
KINO_TOKEN = os.getenv("KINO_TOKEN")
kp = KinopoiskDev(token=KINO_TOKEN)


def upload_image(image):
    response = requests.get(image)
    image_data = response.content
    image_poster = Image.open(BytesIO(image_data))
    image_poster = image_poster.convert("RGB")
    image_bytes = BytesIO()
    image_poster.save(image_bytes, format="JPEG")
    return image_bytes.getvalue()


async def create_date_movie():
    item = await kp.arandom()
    image = []
    for i in item.poster:
        image.append(i[1])
    date_movie = {
        "name": item.name,
        "year": item.year,
        "description": item.description,
        "poster": image[1],
    }
    return date_movie
