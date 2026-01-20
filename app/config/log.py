import logging.config
import os.path

from app.config import BASE_DIR


LOGFILE_DIR = BASE_DIR / 'logs'

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,  # 不禁用现有的日志器
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] %(name)s (%(lineno)d): %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "detailed",
            "filename": LOGFILE_DIR / "app.log",
            "maxBytes": 1024 * 1024 * 5,  # 5MB
            "backupCount": 3,
            "level": "ERROR",
        },
    },
    "loggers": {
        # FastAPI 与 Uvicorn 的日志接管
        "uvicorn": {"handlers": ["console", "file"], "level": "ERROR", "propagate": False},
        "uvicorn.error": {"level": "ERROR"},
        "uvicorn.access": {"handlers": ["console"], "level": "ERROR", "propagate": False},
        # 你的应用自定义日志
        "app": {"handlers": ["console", "file"], "level": "INFO", "propagate": False},
    },
}


def setup_logging():
    if not os.path.exists(LOGFILE_DIR):
        os.makedirs(LOGFILE_DIR)
    logging.config.dictConfig(LOGGING_CONFIG)
