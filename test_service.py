import pytest

from main import service

def test_service():
    res = service()
    assert res["output_rows"] >= 0
