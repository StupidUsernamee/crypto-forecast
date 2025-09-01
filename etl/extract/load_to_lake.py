from env.env import GetEnv

import os
import json
from typing import Any
from datetime import datetime, timezone

class _Saver:
    def __init__(self):
        getEnv = GetEnv()
        self._DATA_DIR = getEnv.get_str("DATA_LAKE_PATH", "./data/raw/BTC/")
        os.makedirs(self._DATA_DIR, exist_ok=True)
    
    def _get_file_path(self):
        now = datetime.now(timezone.utc)
        return os.path.join(
            self._DATA_DIR,
            now.strftime("%Y-%m-%d-%H") + ".jsonl"
        )

    def _append_record(self, record: dict[str, Any]):
        path = self._get_file_path()
        with open(path, 'a') as f:
            f.write(json.dumps(record) + "\n")