import json
import pathlib
from datetime import datetime as dt
from datetime import timezone
from typing import Any
from env.env import GetEnv
from utility.logger_config import Logger

"""
steps:
    1. Get list of data files
    2. Load the current one
    3. Filter the bad features
    4. Return the feature-rich data
"""
class _GetFeatures:

    def __init__(self):
        self._getEnv = GetEnv()
        self._logger = Logger.get_logger("GET_FEATURES")

    def _list_data_files(self) -> list[pathlib.Path]:
        data_path = self._getEnv.get_str("DATA_LAKE_PATH", "") # TODO: fill the fallback value
        files_object = pathlib.Path(data_path)
        files = list(files_object.glob("*.jsonl"))

        return files
    
    def _select_current_file(self, files: list[pathlib.Path]) -> str:
        now = dt.now(timezone.utc)
        format = now.strftime("%Y-%m-%d-%H")
        for file in files:
            if str(file).removesuffix(".jsonl").endswith(format):
                return str(file)
                
        return ""


    def _feature_engineer(self):
        """
            This function opens the files provided from above methods,
            And extracts the features that are useful.
        """
        records = []
        files_list = self._list_data_files()
        file_to_read = self._select_current_file(files_list)
        file = open(file_to_read, 'r')

        for line in file:
            try:
                raw_data = json.loads(line.strip())

            except json.JSONDecodeError as e:
                self._logger.error(f"json encode error: {e}")
                continue

            filtered_data = {
                "name": raw_data.get("name"),
                "symbol": raw_data.get("symbol"),
                "price":raw_data.get("price"),
                "market_cap":raw_data.get("market_cap"),
                "total_volume_24h":raw_data.get("total_volume_24h"),
                "low_24h":raw_data.get("low_24h"),
                "delta_1h": raw_data.get("delta_1h"),
                "delta_24h": raw_data.get("delta_24h"),
                "delta_1h": raw_data.get("delta_1h"),
                "delta_7d": raw_data.get("delta_7d"),
                "delta_30d": raw_data.get("delta_30d"),
                "last_updated_timestamp": raw_data.get("last_updated_timestamp")
            } 
            records.append(filtered_data) 

        file.close()

        return records