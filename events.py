import asyncio
import os
import time
from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel


# Switch between Server and Local
#import env

# Telegram bot setup

target = 'ai_news_flow'
name = 'Serhii_session'
api_id = os.environ['api_id']
api_hash = os.environ['api_hash']
# Ensure channel_id is an integer
target_test_id = int(os.environ['target_test_id'])
interval = os.environ['interval']
last_result = 1


client = TelegramClient(name, api_id, api_hash)




# Sent message to target_test_id
async def sent_message_to_chanell(message):
    await client.send_message(PeerChannel(channel_id=target_test_id), message)






# Async function to check global veriable continuously in the background
async def continuous_ping(interval=float(os.environ.get('interval', 10))):
    while True:

        if os.environ['camera_massage'] != "0":
            await sent_message_to_chanell(os.environ['camera_massage'])
            #os.environ['camera_massage'] = "0"

        await asyncio.sleep(interval)  # Wait for the specified interval


# Main function to run both the bot and the continuous ping
async def main():


    # Start the Telegram bot
    await client.start()


    # Run the continuous checking global veriable in the background
    ping_task = asyncio.create_task(continuous_ping())

    # Run the Telegram bot until it is disconnected
    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
