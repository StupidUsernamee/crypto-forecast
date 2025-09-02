import sys
import logging
from logging.handlers import RotatingFileHandler
from env.env import GetEnv

getEnv = GetEnv()

class Logger:
    _logger = None

    @staticmethod
    def get_logger(name: str = "AppLogger", level=logging.INFO):
        if Logger._logger:
            return Logger._logger
        
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.propagate = False

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
        )
        console_handler.setFormatter(console_formatter)

        file_path = getEnv.get_str("LOG_PATH", "./logs/app.log")
        file_handler = RotatingFileHandler(file_path, maxBytes=5*1024*1024, backupCount=5)
        file_handler.setLevel(level)
        file_handler.setFormatter(console_formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        Logger._logger = logger
        return logger
