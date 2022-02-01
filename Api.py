import datetime
from telethon import TelegramClient, events, sync

import requests
from GameItem import GameItem
from sender import send

def getItemsInQueu():

    headers = {'Content-Type': 'application/json', 'User-Agent': 'BlackDesert'}
    r = requests.post('https://eu-trade.naeu.playblackdesert.com/Trademarket/GetWorldMarketWaitList',headers=headers)

    return r.json()['resultMsg']



# 0 - Item ID
#
# 1 - Enhancement Level
#
# 2 - Price
#
# 3 - Timestamp when item hits the market
#
test = getItemsInQueu()
split_results = test.split("|")

tracked_items = ["705509","705510","705511","705512"]
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

for z in current_market:
    print(z)
    if z.id in tracked_items:
        text = z.name + z.EnchanmentString + " is going to be sold in " +z.getMarketHitTime()
        send(text)




