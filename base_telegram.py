from telethon import TelegramClient, events


async def read_last_message(client, chat_username): # функция которая считывает последнее сообщение
    try:
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

async def send_message_to_user(client, username, message): # функция которая отправляет сообщение пользователю
    try:
        await client.send_message(username, message)
        print("Сообщение отправлено успешно.")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

async def read_and_send_last_message(client, chat_username, receiver_username): # функция которая считывает и отправляет сообщение пользователю
    try:
        last_message = await read_last_message(client, chat_username)
        if last_message:
            await send_message_to_user(client, receiver_username, last_message)
        else:
            print("В беседе нет сообщений.")
    except Exception as e:
        print(f"Произошла ошибка {e}")


async def wait_for_message_from_user(client, user_id): # функция которая ждет сообщение от пользователя
    text_message = ""
    try:
        @client.on(events.NewMessage)
        async def handle_new_message(event):
            if event.from_id == user_id:
                print(f"Получено сообщение от пользователя с ID {user_id}: {event.text}")
                text_message = event.text
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        return text_message