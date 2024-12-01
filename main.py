from dotenv import load_dotenv
from telegram import Bot
import asyncio
import os

# Загрузка переменных окружения
load_dotenv()
group = os.getenv("group")
token = os.getenv("token")


async def send_message_async(bot, chat_id, text):
    """Асинхронно отправить сообщение в канал."""
    await bot.send_message(chat_id=chat_id, text=text)
    print(f"Message sent to {chat_id}: {text}")


def get_directory_from_user():
    """Получает путь к директории от пользователя или использует путь по умолчанию."""
    user_input = input("Введите путь к директории (по умолчанию ./msgs): ").strip()
    return user_input if user_input else "./msgs"


def read_files_from_directory(directory):
    """Читает текст из всех файлов в указанной директории."""
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Директория '{directory}' не найдена.")
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Указанный путь '{directory}' не является директорией.")

    # Получение списка файлов в директории
    file_paths = [
        os.path.join(directory, file_name)
        for file_name in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, file_name))
    ]

    messages = []
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            messages.append(content if content else " ")  # Отправлять пробел, если файл пуст
    return messages


async def send_messages_from_directory(token, group):
    """Получает файлы из директории и отправляет их содержимое как сообщения."""
    bot = Bot(token)
    directory = get_directory_from_user()
    try:
        messages = read_files_from_directory(directory)
        if not messages:
            print(f"В директории '{directory}' нет файлов.")
            return

        for text in messages:
            await send_message_async(bot, group, text)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(send_messages_from_directory(token, group))
