from .fetch_data import read_api
from env.env import GetEnv

import os
import json
from typing import Any
from datetime import datetime, timezone

getEnv = GetEnv()
DATA_DIR = getEnv.get_str("DATA_LAKE_PATH", "./data/raw/BTC/")

os.makedirs(DATA_DIR, exist_ok=True)

def get_file_path():
    now = datetime.now(timezone.utc)
    return os.path.join(
        DATA_DIR,
        now.strftime("%Y-%m-%d-%H") + ".jsonl"
    )


def append_record(record: dict[str, Any]):
    path = get_file_path()
    with open(path, 'a') as f:
        f.write(json.dumps(record) + "\n")