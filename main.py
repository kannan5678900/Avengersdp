import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions
from telethon import TelegramClient, events, sync

try:
    proxy
except NameError:
    proxy = None
print('Logging in Telegram')
client = TelegramClient(config.api_id, config.api_hash, proxy=proxy)
client.start()
print('Logged in as', client.get_me().username)

# Main Function....

COLLECTION_STRING = [
    "avengers-logo-wallpaper",
    "avengers-hd-wallpapers-1080p",
    "avengers-iphone-wallpaper",
    "iron-man-wallpaper-1920x1080",
    "iron-man-wallpapers",
]

async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(url, "f.ttf")
    img = requests.get(fy)
    with open("donottouch.jpg", "wb") as outfile:
        outfile.write(img.content)
    return "donottouch.jpg

        file = await client.upload_file("donottouch.jpg")
        await client(functions.photos.UploadProfilePhotoRequest(file))
        print('Profile Updated!')
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(60)

