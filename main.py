import discord
from discord import Interaction

from dotenv import load_dotenv
from os import getenv

from bot import constants, client
from bot.commands import send_greetings
from logger.logger import Logger

load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")
GUILD = discord.Object(id=constants.GUILD)

unforgiv3n_client = client.Client()
tree = unforgiv3n_client.tree
logger = Logger()


@tree.command(guild=GUILD, name="introduce", description="Meet the bot")
async def say_hi(interaction: Interaction) -> None:
    log_channel = unforgiv3n_client.get_channel(constants.LOGGING_CHANNEL_ID)
    await send_greetings(logger, log_channel, interaction)

unforgiv3n_client.run(TOKEN)