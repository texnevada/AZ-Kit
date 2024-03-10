import logging
import datetime

from tools.functions import settings


def az_get_log(name: str):
    user_settings = settings.load_user_settings()
    logger = logging.getLogger(name)
    # logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | [%(levelname)s] | %(name)s: %(message)s')
    stream_formatter = logging.Formatter('%(message)s')

    # print(config["Logging"]["Azure_API_log_to_file"].lower())
    if user_settings["Azure_API_log_to_file"]["enabled"] is True:
        now = datetime.datetime.now()
        time = now.strftime("%-d.%-m.%-y")
        log_file = user_settings["logging_folder"]["value"]
        file_handler = logging.FileHandler(f"{log_file}/AzureAPI_{time}.log")
        file_handler.setLevel(0)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # print(config["Logging"]["Azure_API_log_to_console"].lower())
    if user_settings["Azure_API_log_to_console"]["enabled"] is True:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(stream_formatter)
        stream_handler.setLevel(0)
        logger.addHandler(stream_handler)
    return logger
