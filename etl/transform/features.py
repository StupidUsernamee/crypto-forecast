import os
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
        self._logger = Logger()

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
        records = []
        files_list = self._list_data_files()
        file_to_read = self._select_current_file(files_list)
        with open(file_to_read, 'r') as file:
            pass



if __name__ == "__main__":
    a = _GetFeatures()
    a._list_data_files()