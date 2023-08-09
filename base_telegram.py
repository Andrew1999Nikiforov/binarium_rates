from telethon import events
import socket

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

async def read_and_send_last_message(client, chat_username, receiver_username): # функция которая считывает и отправляет сообщение пользователю 2 в 1
    try:
        last_message = await read_last_message(client, chat_username)
        if last_message:
            await send_message_to_user(client, receiver_username, last_message)
        else:
            print("В беседе нет сообщений.")
    except Exception as e:
        print(f"Произошла ошибка {e}")

async def send_message_to_user(client, username, message): # функция которая отправляет сообщение пользователю
    try:
        await client.send_message(username, message)
        print("Сообщение отправлено успешно.")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

async def send_text_to_program_y(text): # Функция отвечающая за отправку данных второй программе
    server_address = ('localhost', 14777)  # Укажите адрес и порт сервера программы Y
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(text.encode('utf-8'), server_address)

async def wait_for_message_from_user(client, user_id): # функция которая ждет сообщение от пользователя
    try:
        await client.start()
        client.add_event_handler(lambda event: send_text_to_program_y(event.text), events.NewMessage(chats=user_id))
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        await client.disconnect()
        