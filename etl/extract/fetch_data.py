import requests
import json
from typing import Any


def read_api(url: str, params: dict) -> dict[str, Any]:
    try: 
        resp = requests.get(url=url, params=params)

        data = resp.json()

        return data

    except json.JSONDecodeError as e:
        print(f"Cannot decode, err: {e}")
        return dict()