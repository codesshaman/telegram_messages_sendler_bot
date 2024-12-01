from dotenv import load_dotenv
from apis.messages import *
from telegram import Bot
import asyncio
import os

load_dotenv()

group = os.getenv("group")
token = os.getenv("token")


async def send_message_async(token, chat_id, text):
    """Асинхронно отправить сообщение в канал."""
    bot = Bot(token)
    await bot.send_message(chat_id=chat_id, text=text)
    print(f"Message sent to {chat_id}")

if __name__ == "__main__":
    message_text = "Hello, this is a test message from python-telegram-bot with asyncio!"
    
    asyncio.run(send_message_async(token, group, message_text))
