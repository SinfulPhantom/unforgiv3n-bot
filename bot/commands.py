import inspect

from models.logger_model import LoggerConstructor
from utils.text_formatter import get_full_method
from utils.trace_back import send_error, get_traceback


async def send_greetings(misery_logger, log_channel, interaction):
    current_method_name = get_full_method(inspect.stack()[0][3])
    try:
        await interaction.response.send_message("Hello everyone, I'm Unforgiv3n Bot!")
        await misery_logger.send(
            log_channel=log_channel,
            log=LoggerConstructor(
                title=current_method_name,
                description="This is a friendly reminder that bots are our friends :heart:",
                level="info",
            ),
        )
    except Exception as e:
        await misery_logger.send(
            log_channel=log_channel,
            log=send_error(current_method_name, e.__str__(), get_traceback(e)),
        )
