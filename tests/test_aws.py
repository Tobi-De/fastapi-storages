from pathlib import Path

from fastapi_storages import  LocalStorageBackend

import pytest
import tempfile


@pytest.fixture()
def local_():
    tmp_dir = Path("media")
    tmp_dir.mkdir()
    yield LocalStorageBackend(dir=tmp_dir)
    tmp_dir.unlink()


def test_local_initialization(local):
    tmp_file = tempfile.SpooledTemporaryFile()
