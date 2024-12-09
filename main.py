import os
import re
import time
import asyncio
from dotenv import load_dotenv
from aiogram import Bot

# Загружаем переменные из .env
load_dotenv()
token = os.getenv("token")
group = os.getenv("group")

# Инициализация бота
bot = Bot(token)

# Функция для экранирования текста в формате MarkdownV2, кроме скрытого текста
def escape_markdown_v2(text):
    """Экранирует символы MarkdownV2 для безопасной отправки в Telegram, кроме скрытого текста."""
    # Экранируем все специальные символы MarkdownV2
    text = re.sub(r'([_\*\[\]\(\)\~\`\>\#\+\-\=\|\,\.\!\&])', r'\\\1', text)
    # Снимаем экранирование для символов, относящихся к скрытому тексту
    text = text.replace(r'\|\|', '||')
    return text

async def send_messages_from_directory():
    """Получает файлы из директории и отправляет их содержимое как сообщения."""
    # Путь к директории
    directory = input("Введите путь к директории (по умолчанию ./msgs): ").strip() or "./msgs"
    
    if not os.path.exists(directory):
        print(f"Директория '{directory}' не найдена.")
        return

    # Чтение текстов из файлов
    file_paths = [
        os.path.join(directory, file_name)
        for file_name in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, file_name))
    ]
    
    if not file_paths:
        print(f"В директории '{directory}' нет файлов.")
        return

    for file_path in file_paths:
        time.sleep(1)
        file_name = os.path.basename(file_path).rsplit('.', 1)[0]  # Имя файла без расширения
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            # Если файл пустой, отправляем пробел
            if not content:
                content = " "

            # Экранируем только специальные символы Markdown, кроме || для скрытого текста
            formatted_text = escape_markdown_v2(content)

            # Отправка имени файла и содержимого
            try:
                # Отправляем имя файла
                await bot.send_message(group, f"*{escape_markdown_v2(file_name)}*", parse_mode='MarkdownV2')
                print(f"Имя файла отправлено: {file_name}")

                # Отправляем содержимое файла
                await bot.send_message(group, formatted_text, parse_mode='MarkdownV2')
                print(f"Содержимое файла отправлено: {formatted_text}")
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")

async def main():
    await send_messages_from_directory()

if __name__ == "__main__":
    asyncio.run(main())
