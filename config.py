import os



class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")

    # Authorized user ids to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # superusers to broadcast messages & fetch subscribers count
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")

    # Force subscribe channel / group id starting with -100
    FORCE_SUB_CHAT = os.environ.get("FORCE_SUB_CHAT", "")

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000
