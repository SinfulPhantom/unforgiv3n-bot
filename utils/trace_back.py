import traceback
from models.logger_model import LoggerConstructor


def get_traceback(e):
    error_traceback = (
        "Traceback (most recent call last):\n"
        + "".join(traceback.format_list(traceback.extract_tb(e.__traceback__)))
        + type(e).__name__
        + ": "
        + str(e)
    )
    return error_traceback


def send_error(method, error, trace):
    return LoggerConstructor(
        title=method,
        description=error,
        error=trace,
    )
