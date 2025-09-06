from datetime import datetime, timezone

from clean import _CleanData
from features import _GetFeatures
from utility.logger_config import Logger

class Transform:

    def __init__(self):
        self._logger = Logger.get_logger("ETL: transform")
        self._cleaner = _CleanData()
        self._feature_engineer = _GetFeatures() 


    def run(self):
        try:
            filtered_records = self._feature_engineer._feature_engineer()
            cleaned_records = self._cleaner.clean(filtered_records)
            hour = datetime.now(timezone.utc).hour 
            self._logger.info(f"transofrm of batch:hour:{hour-1} completed")
            return cleaned_records

        except Exception as e:
            self._logger.error(f"unexpected error: {e}")