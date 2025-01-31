import datetime, discord
from constants import DISCORD_TOKEN
from utils import process_message

# Define the Discord client with intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

# Define an event handler for when the client connects to Discord
@client.event
async def on_ready():
    print("Logged in as {0.user}.".format(client))
    print(datetime.datetime.now())

# Define an event handler for when a message is sent in a channel
@client.event
async def on_message(message):
    print("hello")
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    
    # check if the message is a command
    if message.content.startswith("!"):
        await process_message(message)


# Run the client with the Discord API token
client.run(DISCORD_TOKEN)