from .fetch_data import read_api

import json
from typing import Any

def load_data(path: str, url: str, params: dict[str, Any]):
    
    data_to_load = read_api(url=url, params=params)

    with open(path, "a", encoding="utf-8") as file:
        json.dump(data_to_load, file)
        file.write("\n")
        print("data saved to file")
