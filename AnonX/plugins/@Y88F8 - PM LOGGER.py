from pyrogram import Client, filters
session = "" # Pyrogram String Session Here
api_id = 1234567 # API ID HERE
api_hash = "API_HASH"

app = Client(
   "Session Name",
    api_id=api_id,
  api_hash=api_hash,
  session_string=session
  )
  
LOG = -1001702582034 # Log group id
@app.on_message(filters.private)
async def logger(client, message):
      me = (await client.get_me()).id
      if message.from_user.id == me:
        return
      to_chat = LOG
      from_chat = message.from_user.id
      d = message.id
      await app.forward_messages(
           to_chat,
           from_chat,
           d
      )
      
print("🟢")
app.run()   
      
