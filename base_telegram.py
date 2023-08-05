

async def read_last_message(client, chat_username):
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

async def send_message_to_user(client, username, message):
    try:
        await client.send_message(username, message)
        print("Сообщение отправлено успешно.")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

async def read_and_send_last_message(client, chat_username, receiver_username):
    try:
        last_message = await read_last_message(client, chat_username)
        if last_message:
            await send_message_to_user(client, receiver_username, last_message)
        else:
            print("В беседе нет сообщений.")
    except Exception as e:
        print(f"Произошла ошибка {e}")