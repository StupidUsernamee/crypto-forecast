import requests
import json
from typing import Any
from env.env import GetEnv
from utility.logger_config import Logger


class _Fetcher:
    def __init__(self):
        getEnv = GetEnv()
        self._logger = Logger.get_logger(name="FETCH_DATA")
        self._url = getEnv.get_str("API_URL", "")
        self._params = {
            "key": getEnv.get_str("API_KEY", ""),
            "pref": getEnv.get_str("API_PREF", ""),
            "symbol": getEnv.get_str("API_SYMBOL", "")
        }
    
    def _fetch_data(self) -> tuple[dict[str, Any], int]:
        try:
            resp = requests.get(url=self._url, params=self._params)

            if resp.status_code == 429:
                return (dict(), 429)

            data = resp.json()
            return (data, resp.status_code)
        
        except json.JSONDecodeError as e:
            self._logger.error(f"Cannot decode, err: {e}")
            return (dict(), 403)