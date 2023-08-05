from telethon.sync import TelegramClient
from telethon import TelegramClient, events, types
import dialogs
import base_telegram
import param

client = TelegramClient(param.password.name_session, param.password.api_id, param.password.api_hash, \
                        system_version=param.password.system_version, \
                        device_model=param.password.device_model, app_version=param.password.app_version)

chat_username = param.username.get_message_username
receiver_username = param.username.receiver_username

# Функция для печати списка чатов и диалогов
with client:
   client.loop.run_until_complete(dialogs.print_dialogs(client))

with client:
    client.loop.run_until_complete(base_telegram.read_and_send_last_message(client, chat_username, receiver_username))


