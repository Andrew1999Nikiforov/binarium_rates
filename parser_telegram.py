from telethon.sync import TelegramClient
from telethon import TelegramClient
import base_telegram
import param

client = TelegramClient(param.password.name_session, param.password.api_id, param.password.api_hash, \
                        system_version=param.password.system_version, \
                        device_model=param.password.device_model, app_version=param.password.app_version)

chat_username = param.username.get_message_username
receiver_username = param.username.receiver_username

with client: # функция которая ждет сообщение от пользователя
    client.loop.run_until_complete(base_telegram.wait_for_message_from_user(client, param.username.get_message_username))

#with client: # функция которая отправляет сообщение пользователю
#    client.loop.run_until_complete(base_telegram.send_message_to_user(client, param.username.receiver_username, "222"))

#with client: # Вызов функции для печати списка чатов и диалогов
#   client.loop.run_until_complete(dialogs.print_dialogs(client))

#with client: # Вызов функции которая читает последнее собщение и отправляет другому пользователю
#    client.loop.run_until_complete(base_telegram.read_and_send_last_message(client, chat_username, receiver_username))