from pyrogram import Client, filters
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
source_chat = os.environ["SOURCE_CHAT"]
target_chat = int(os.environ["TARGET_CHAT"])

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(source_chat))
def forward(client, message):
    print(f"📨 Пересылаем сообщение: {message.text[:40]}...")
    message.forward(target_chat)

app.run()
