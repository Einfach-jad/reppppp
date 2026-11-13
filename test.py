import os
import discord

TOKEN = os.environ["TOKEN"]
CHANNEL_ID = 1569454134766342345

client = discord.Client()

@client.event
async def on_ready():
    print(f"Eingeloggt als {client.user}")
    await client.ws.voice_state(None, CHANNEL_ID, self_mute=True, self_deaf=True)
    print("Im Call, fullmute.")

client.run(TOKEN)