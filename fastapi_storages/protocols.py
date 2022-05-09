from pathlib import Path
from typing import Protocol

File = str

from storages.backends.s3boto3 import S3Boto3Storage

class StorageBackend(Protocol):
    destination_path: Path

    async def write(self, file: File):
        pass

    async def read(self, ):
        pass
