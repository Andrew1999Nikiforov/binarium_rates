from telethon import events
import re

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

async def check_exit(event, client): # выход из программы
    if("exit" in str(event)): 
        await client.disconnect()

async def send_message_to_user(client, username, message): # функция которая отправляет сообщение пользователю
    try:
        await client.send_message(username, message)
        print("Сообщение отправлено успешно.")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

def parse_message(message): # Функция которая обрабатывает строку с канала
    pattern = r'([A-Za-z]+)\s+(\d{2}:\d{2})\s+(вверх|вниз)'
    match = re.match(pattern, message)
    if match:
        return match.group(1), match.group(2), match.group(3)
    else:
        return None

message1 = "Bitcoin 15:00 вверх"

parsed_message1 =  parse_message(message1)

print(parsed_message1)  # ('Bitcoin', '15:00', 'вверх')

async def handle_new_message(event, client): # проверка сообщения на корректность
    await check_exit(event.text, client) # Выход из программы (Потом убрать)
    #await send_message_to_user(client, param.username.receiver_username, event.text) # Пересылаем это письмо другому человеку (Потом убрать)
    print(f"Получено сообщение от пользователя с ID {event.chat.title}: {event.text}")



async def wait_for_message_from_user(client, user_id): # функция которая ждет сообщение от пользователя
    try:
        await client.start()
        client.add_event_handler(lambda event: handle_new_message(event, client), events.NewMessage(chats=user_id))
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        await client.disconnect()
        