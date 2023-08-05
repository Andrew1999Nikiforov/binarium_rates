from telethon.sync import TelegramClient
from telethon import TelegramClient, events, types
from dialogs import dialogs
import param

client = TelegramClient(param.password.name_session, param.password.api_id, param.password.api_hash, \
                        system_version=param.password.system_version, \
                        device_model=param.password.device_model, app_version=param.password.app_version)

async def read_last_message(chat_username):
    try:
        await client.start()
        chat = await client.get_entity(chat_username)  
        messages = await client.get_messages(chat, limit=1)
        if messages:
            last_message = messages[0]
            print(last_message.text)
            return last_message.text
        else:
            return None
    except Exception as e:
            print(f"Ошибка при чтении последнего сообщения: {e}")
    finally:
        await client.disconnect()

async def send_message_to_user(username, message):
    try:
        await client.start()
        await client.send_message(username, message)
        print("Сообщение отправлено успешно.")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")
    finally:
        await client.disconnect()

async def read_and_send_last_message(chat_username, receiver_username):
    try:
        last_message = await read_last_message(chat_username)
        if last_message:
            await send_message_to_user(receiver_username, last_message)
        else:
            print("В беседе нет сообщений.")
    except Exception as e:
        print(f"Произошла ошибка {e}")
    finally:
        await client.disconnect()

chat_username = param.username.get_message_username
receiver_username = param.username.receiver_username

#with client:
 #   client.loop.run_until_complete(read_and_send_last_message(chat_username, receiver_username))


# Функция для печати списка чатов и диалогов
with client:
    client.loop.run_until_complete(dialogs.print_dialogs(client))
