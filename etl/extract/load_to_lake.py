from .fetch_data import read_api

import json

def load_data(path: str):
    url = "https://coinlib.io/api/v1/coin"
    params = {
        "key": "76a7b7c3459c54d4",
        "pref": "USDT",
        "symbol": "BTC"
    }
    data_to_load = read_api(url=url, params=params)

    with open(path, "a", encoding="utf-8") as file:
        json.dump(data_to_load, file)
        file.write("\n")
        print("data saved to file")
