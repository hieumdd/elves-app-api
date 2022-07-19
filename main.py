from typing import Any

from compose import compose

from repo import get
from bigquery import load
from pipeline import transform, schema


def service():
    return compose(
        lambda x: {"output_rows": x},
        load("Analytics", schema),
        transform,
        get,
    )()


def main(request):
    response = service()

    print(response)
    return response
