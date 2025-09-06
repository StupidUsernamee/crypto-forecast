from typing import Any

from utility.logger_config import Logger

class _CleanData:
    def __init__(self):
        self._logger = Logger.get_logger(name="CLEAN_DATA")

    
    def clean(self, records: list[dict]) -> list[dict]:

        cleaned = []        
        for r in records:
            r = self._handle_missing_values(r)
            r = self._normalize_types(r)
            if r is not None:
                cleaned.append(r)
        
        return cleaned
        

    def _handle_missing_values(self, record: dict | None) -> dict | None:

        if record is None:
            return None

        for _, val in record.items():
            if (val == "") or (val == None):
                return None
        
        return record


    def _normalize_types(self, record: dict | None) -> dict | None:

        if record is None:
            return None

        try:

            record["price"] = float(str(record.get("price")).replace(",", "."))   
            record["market_cap"] = float(str(record.get("market_cap")).replace(",", "."))   
            record["low_24h"] = float(str(record.get("low_24h")).replace(",", "."))
            record["high_24h"] = float(str(record.get("high_24h")).replace(",", "."))
            record["delta_24h"] = float(str(record.get("delta_24h")).replace(",", "."))
            record["delta_7d"] = float(str(record.get("delta_7d")).replace(",", "."))
            record["delta_30d"] = float(str(record.get("delta_30d")).replace(",", "."))
            record["last_updated_timestamp"] = int(str(record.get("last_updated_timestamp")))

            return record

        except TypeError as e:
            self._logger.error(f"cannot normalize record types, bad record detected, error: {e} ")
            return None