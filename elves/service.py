from compose import compose

from elves.pipeline import interface
from elves import repo
import bigquery


def service(pipeline: interface.Pipeline):
    return compose(
        lambda x: {"output_rows": x},
        bigquery.load("Analytics", pipeline.schema),
        repo.get,
    )(pipeline.url)
