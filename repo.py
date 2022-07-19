from typing import Any
import os

import httpx


def get() -> list[dict[str, Any]]:
    r = httpx.get(
        "https://api.elvesapp.com/api/utils/analytics/requests",
        headers={"Authorization": os.getenv("TOKEN", "")},
    )
    data = r.json()
    return data
