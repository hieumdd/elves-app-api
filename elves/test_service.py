import pytest

from elves.pipeline import pipelines
from elves.service import service


@pytest.mark.parametrize(
    "pipeline",
    pipelines.values(),
    ids=pipelines.keys(),
)
def test_service(pipeline):
    res = service(pipeline)
    assert res["output_rows"] >= 0
