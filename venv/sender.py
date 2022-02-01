from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
def sendMessage(msg):
    api_id = 18152008
    api_hash = 'c692c0db55d6408f674a400f1d8ac478'

    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    target = client.get_entity("@warrisivirus")
    client.send_message(target,msg)