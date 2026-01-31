import os.path
from pathlib import Path
import dotenv


BASE_DIR = Path(__file__).resolve().parent.parent


envpath = BASE_DIR / ".env"
if os.path.exists(envpath):
    dotenv.load_dotenv(envpath)


CORS = {
    'allow_origins': ["*"],
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"],
}

COOKIE_DOMAIN = os.getenv("AUTH_COOKIE_DOMAIN", "userver.test")
COOKIE_KEY = os.getenv("AUTH_COOKIE_KEY", "token")
TOKEN_EXPIRE = 60 * 60 * 2  # s

HEADER_KEY = "Authorization"
API_KEY = os.getenv("AUTH_API_KEY", "bk-b5522a629960db12bfdfe89eab77247689c65ba2e03bd611f73555954f14fbb0")
