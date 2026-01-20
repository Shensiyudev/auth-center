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
