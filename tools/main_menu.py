#!/usr/bin/env python3

from tools.generic_functions import check, cursor, settings
from tools.generic_functions.clear import clear
from tools.generic_functions.setup_logger import get_log

init(autoreset=True)
logger = get_log(__name__)
account_cache = []

def start():
    information_bar()

def information_bar():
    user_settings = settings.load_user_settings()

    # Response 0 = Subscription
    # Response 1 = Account
    # Response 2 = Subscription ID
    response = account.check_account()
    current_version = check.current_version()
    account_cache.clear()
    account_cache.append(response)
    clear()

    logger.info("#"*79)