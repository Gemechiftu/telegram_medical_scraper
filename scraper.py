from telethon.sync import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH

client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)

async def main():
    me = await client.get_me()
    print(me.stringify())

with client:
    client.loop.run_until_complete(main())
