import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv('API_KEY')
YANDEX_API_KEY = os.getenv('YANDEX_API_KEY')