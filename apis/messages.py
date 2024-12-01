import requests

class Messages:
    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, text):
        """Отправить сообщение в группу."""
        url = f"{self.base_url}/sendMessage"
        params = {
            "chat_id": self.group_id,
            "text": text
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to send message", "status_code": response.status_code}

    def get_chat_info(self):
        """Получить информацию о группе."""
        url = f"{self.base_url}/getChat"
        params = {
            "chat_id": self.group_id
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to get chat info", "status_code": response.status_code}

    def delete_message(self, message_id):
        """Удалить сообщение по его ID."""
        url = f"{self.base_url}/deleteMessage"
        params = {
            "chat_id": self.group_id,
            "message_id": message_id
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to delete message", "status_code": response.status_code}

    def get_messages(self):
        """Получить последние сообщения из группы."""
        url = f"{self.base_url}/getUpdates"
        params = {
            "chat_id": self.group_id
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to get messages", "status_code": response.status_code}
    
    def edit_message(self, message_id, new_text):
        """Изменить текст сообщения."""
        url = f"{self.base_url}/editMessageText"
        params = {
            "chat_id": self.group_id,
            "message_id": message_id,
            "text": new_text
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to edit message", "status_code": response.status_code}
    
    def get_admins(self):
        """Получить список администраторов в группе."""
        url = f"{self.base_url}/getChatAdministrators"
        params = {
            "chat_id": self.group_id
        }
        response = requests.get(url, params=params)  # Используем GET-запрос
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to get chat administrators", "status_code": response.status_code}

    # Получить обновления, чтобы проверить правильность chat_id
    def get_updates(self):
        """Получить обновления."""
        url = f"{self.base_url}/getUpdates"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to get updates", "status_code": response.status_code}
