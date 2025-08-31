import os
import logging

from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)

class GetEnv():

    def __init__(self):
        load_dotenv()

    def get_str(self, key: str, fallback: str) -> str:
        val = os.getenv(key)

        if val is None:
            logging.warning(f"env[{key}] not found, using fallback value: {fallback}")
            return fallback
        
        logging.info(f" key[{key}]: {val}")
        return val


    def get_int(self, key: str, fallback: int) -> int:
        val = os.getenv(key)

        if val is None:
            logging.warning(f"env[{key}] not found, using fallback value: {fallback}")
            return fallback

        try:
            int_val = int(val)
            logging.info(f" key[{key}]: {val}")
            return int_val
        except ValueError:
            logging.warning(f"env[{key}] invalid value, has to be int, using fallback value: {fallback}")
            return fallback

    
    def get_bool(self, key: str, fallback: bool) -> bool:
        val = os.getenv(key)

        if val is None:
            logging.warning(f"env[{key}] not found, using fallback: {fallback}")
            return fallback
        
        if val.lower() in ("yes", "1", "true"):
            logging.info(f" key[{key}]: {val}")
            return True

        if val.lower() in ("no", "0", "false"):
            logging.info(f" key[{key}]: {val}")
            return False
        
        logging.warning(f"env[{key}] invalid value, has to be bool, using fallback value: {fallback}")
        return fallback

