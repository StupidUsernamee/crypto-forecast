import requests
import json
from typing import Any


def read_api(url: str, params: dict) -> tuple[dict[str, Any], int]:
    try: 
        resp = requests.get(url=url, params=params)

        data = resp.json()

        return (data, resp.status_code)

    except json.JSONDecodeError as e:
        print(f"Cannot decode, err: {e}")
        return (dict(), 403)