from telethon import types

class dialogs(): 
    async def print_dialogs(client): # Функция выводящая информацию про 10 групп и бесед
        try:
            dialogs = await client.get_dialogs(limit=10)
            for dialog in dialogs:
                entity = dialog.entity
                if isinstance(entity, types.User):
                    if entity.username:
                        print(f"Имя: {entity.first_name} {entity.last_name}, Username: @{entity.username}")
                    else:
                        print(f"Имя: {entity.first_name} {entity.last_name}, ID: {entity.id}")
                elif isinstance(entity, types.Chat):
                        print(f"Название чата: {entity.title}, ID: {entity.id}")
                elif isinstance(entity, types.Channel):
                    if entity.username:
                        print(f"Название канала: {entity.title}, Username: @{entity.username}")
                    else:
                        print(f"Название канала: {entity.title}, ID: {entity.id}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            await client.disconnect()