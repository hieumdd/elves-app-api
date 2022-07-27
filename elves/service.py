from compose import compose

from elves.pipeline import interface
from elves import repo
import bigquery


def service(pipeline: interface.Pipeline):
    return compose(
        lambda x: {"output_rows": x},
        bigquery.load(pipeline.name, pipeline.schema),
        pipeline.transform,
        repo.get,
    )(pipeline.url)
