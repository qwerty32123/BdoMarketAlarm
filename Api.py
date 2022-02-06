import datetime
import time
from random import randint
from telethon import TelegramClient, events, sync
import requests
from GameItem import GameItem
from sender import send
import telethon
from bot import run
def getItemsInQueu():
    headers = {'Content-Type': 'application/json', 'User-Agent': 'BlackDesert'}
    r = requests.post('https://eu-trade.naeu.playblackdesert.com/Trademarket/GetWorldMarketWaitList',headers=headers)
    return r.json()['resultMsg']


tracked_items = ["705509","705510","705511","705512"]
blacklist = ["719901","719902","719903","719904"]
timestamps = []
while True:
# 0 - Item ID
#
# 1 - Enhancement Level
#
# 2 - Price
#
# 3 - Timestamp when item hits the market

    try:
        time.sleep(60)
        test = getItemsInQueu()
        split_results = test.split("|")

        current_market = []
        for p in split_results:
            result = p.split("-")
            if len(result) == 4:
                item_id = result[0]
                enchantment_level = result[1]
                price = result[2]
                timestamp_sell = result[3]
                now = datetime.datetime.now()
                Item = GameItem(item_id,enchantment_level,price,timestamp_sell,now)
                current_market.append(Item)
        if len(current_market) == 0:
            timestamps = []
        print(current_market)
        tracked_item_count = 0
        for z in current_market:
            if z.id in tracked_items or ('Blackstar' in z.name and z.id not in blacklist):
                tracked_item_count = tracked_item_count +1
                time = z.getMarketHitTime()
                if time not in timestamps:

                    text = z.name + z.EnchanmentString + " is going to be sold in " +z.getMarketHitTime() + "for "+ z.price
                    send(text)
                    run(text,z.item_type)
        if tracked_item_count == 0:
            timestamps = []
    except Exception:
        continue

