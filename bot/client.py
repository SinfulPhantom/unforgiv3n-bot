import discord
from discord import app_commands
from datetime import datetime
from bot import constants

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.voice_states = True


class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(intents=intents, *args, **kwargs)
        self.tree = app_commands.CommandTree(self)
        self.guild = discord.Object(id=constants.GUILD)

    async def on_ready(self):
        await self.wait_until_ready()
        try:
            await self.tree.sync(guild=self.guild)
            print("Commands are now synced to the server!")
        except Exception as e:
            print(f"{e}|{type(e)}")
        print(
            f"We have logged in as {self.user} on {datetime.now().strftime('%A %d-%m-%Y, %H:%M:%S')}"
        )
