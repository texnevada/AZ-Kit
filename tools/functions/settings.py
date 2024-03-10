import json

from tools.functions import check


def load_user_settings():
    file_location = "./user_settings.json"
    try:
        with open(file_location, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(file_location, "w") as f:
            new_user_settings = default_user_settings().copy()
            if check.system(platform="darwin") is True:
                new_user_settings["emojis_in_menu"]["enabled"] = False
            json.dump(new_user_settings, f)

        return new_user_settings


def toggle_enabled(setting_key: str, value: bool):
    file_location = "./user_settings.json"
    with open(file_location, "r") as f:
        settings = json.load(f)
    settings[setting_key]["enabled"] = value
    with open(file_location, "w") as f:
        json.dump(settings, f)


def change_int_value_setting(setting_key: str, value: int):
    file_location = "./user_settings.json"
    with open(file_location, "r") as f:
        settings = json.load(f)
    settings[setting_key]["value"] = value
    with open(file_location, "w") as f:
        json.dump(settings, f)


def change_str_value_setting(setting_key: str, value: str):
    file_location = "./user_settings.json"
    with open(file_location, "r") as f:
        settings = json.load(f)
    settings[setting_key]["value"] = value
    with open(file_location, "w") as f:
        json.dump(settings, f)


def default_user_settings():
    # Define default settings
    settings = {

        # Toggle settings
        "ascii_splash": {
            "name": "Ascii splash screen",
            "enabled": True,
            "hidden": False
        },
        "emojis_in_menu": {
            "name": "Emojis in the menus",
            "enabled": True,
            "hidden": False
        },
        "no_subscriptions_list": {
            "name": "Tenants with no subscriptions to appear when re-authenticating",
            "enabled": False,
            "hidden": False
        },
        "Azure_API_log_to_file": {
            "name": "Azure API logs to file (Enabling this will store secrets to file!! Used for debugging)",
            "enabled": False,
            "hidden": False
        },
        "Azure_API_log_to_console": {
            "name": "Azure API logs to console (Will bloat console output. Used for debugging)",
            "enabled": False,
            "hidden": False
        },
        "logging": {
            "name": "Logs to file (Will log INFO & Debug messages to file)",
            "enabled": False,
            "hidden": False
        },

        # These are the logger codes used by the logging system.
        # CRITICAL = 50
        # ERROR = 40
        # WARNING = 30
        # INFO = 20
        # DEBUG = 10
        # NOTSET = 0
        "logging_level": {
            "name": "Logging level",
            "type": "int",
            "value": 10,
            "hidden": False
        },
        "console_logging_level": {
            "name": "Console logging level",
            "type": "int",
            "value": 20,
            "hidden": False
        },
        "logging_folder": {
            "name": "Logging location",
            "type": "str",
            "value": "./logs",
            "hidden": False
        },
    }
    return settings


