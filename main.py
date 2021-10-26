import asyncio
import os
import random
import re
import urllib
import requests

from pyrogram import Client, filters

Avengers=Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"],
    session_name = os.environ["SESSION_NAME"]
)

COLLECTION_STRING = [
    "peter-parker-hd-4k-wallpapers",
    "avengers-logo-wallpaper",
    "avengers-hd-wallpapers-1080p",
    "avengers-iphone-wallpaper",
    "iron-man-wallpaper-1920x1080",
    "iron-man-wallpapers",
    "spider-man-hd-4k-wallpapers",
]

def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf", "f.ttf")
    img = requests.get(fy)
    with open("donottouch.jpg", "wb") as outfile:
        outfile.write(img.content)
    return "donottouch.jpg"

@Avengers.on_message(filters.command("avengers"))
async def Avengers_main(client, message):
    await message.reply(
        "**Starting Avengers Profile Pic...\n\nDone !!! Check Your DP in 5 seconds.**")

    while True:
        if Avengers.is_connected:
            await animepp()
            file = await Avengers.set_profile_photo(photo="donottouch.jpg")        
            me = await Avengers.get_me()
            photos = await Avengers.get_profile_photos("me")           
            os.system("rm -rf donottouch.jpg")
            try:
                await Avengers.delete_profile_photos(photos[1].file_id)
            except Exception:
                pass        
            print("Profile Updated!")
        await asyncio.sleep(300)     

print("☄️ AVENGERS ASSEMBLE! ☄️")
Avengers.run()
