import os
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
BOT_USERNAME = os.getenv('TELEGRAM_BOT_USERNAME')
