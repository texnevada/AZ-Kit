import logging
import datetime

from tools.functions import settings


def get_log(name: str):
    user_settings = settings.load_user_settings()
    logger = logging.getLogger(name)
    # logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | [%(levelname)s] | %(name)s: %(message)s')
    stream_formatter = logging.Formatter('%(message)s')

    if user_settings["logging"]["enabled"] is True:
        now = datetime.datetime.now()
        time = now.strftime("%-d.%-m.%-y")
        log_file = user_settings["logging_folder"]["value"]
        file_handler = logging.FileHandler(f"{log_file}/runtime_{time}.log")
        file_handler.setLevel(user_settings["logging_level"]["value"])
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_formatter)
    stream_handler.setLevel(user_settings["console_logging_level"]["value"])
    logger.addHandler(stream_handler)
    return logger
