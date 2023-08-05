from telethon.sync import TelegramClient
import param

client = TelegramClient(param.password.name_session, param.password.api_id, param.password.api_hash, \
                        system_version=param.password.system_version, \
                        device_model=param.password.device_model, app_version=param.password.app_version)

async def read_last_message():
    await client.start()
    chat = await client.get_entity(param.username.get_message_username)  
    messages = await client.get_messages(chat, limit=1)
    if messages:
        last_message = messages[0]
        print(last_message.text)
    else:
        print("No messages found in the chat.")
    await client.disconnect()

with client:
    client.loop.run_until_complete(read_last_message())

