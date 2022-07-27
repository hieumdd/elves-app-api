from typing import Any
import os

import httpx


def get(url: str) -> list[dict[str, Any]]:
    r = httpx.get(
        url,
        headers={"Authorization": os.getenv("API_TOKEN", "")},
        timeout=None,
    )
    data = r.json()
    return data
