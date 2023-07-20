from bot import constants
from discord import Embed
from models.logger_model import LoggerConstructor
from utils.text_formatter import code, tag_role


class Logger:
    async def send(self, log_channel, log: LoggerConstructor) -> None:
        _level = log.level
        if log.error:
            _level = "error"

        _color = constants.COLORS.get(_level)
        _title = f"{constants.EMOJIS.get(_level)} {log.title}"
        _description = log.description

        message_embed = Embed(title=_title, description=_description, color=_color)
        message_embed.set_author(name="Logging Service", icon_url=constants.icon_url)

        if log.error:
            message_embed.add_field(
                name="Error", value=code(str(log.error)), inline=False
            )
            message_embed.add_field(
                name=constants.line_break,
                value=tag_role(constants.STAFF_ROLE_ID),
                inline=True
            )

        await log_channel.send(embed=message_embed)
