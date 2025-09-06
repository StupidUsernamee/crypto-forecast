from .fetch_data import _Fetcher
from .load_to_lake import _Saver

from utility.logger_config import Logger


class Extract:
    # TODO: err hgandling
    def __init__(self):
        self._fetcher = _Fetcher()
        self._saver = _Saver()

        self._logger = Logger.get_logger("etl: EXTRACT")

    def run(self):
        data, _ = self._fetcher._fetch_data()
        self._saver._append_record(data)
        self._logger.info("data added to data lake")