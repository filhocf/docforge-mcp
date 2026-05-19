from .azure import upload_to_azure
from .gcs import upload_to_gcs
from .local import upload_to_local_folder
from .minio import upload_to_minio
from .s3 import upload_to_s3

__all__ = [
    "upload_to_local_folder",
    "upload_to_s3",
    "upload_to_gcs",
    "upload_to_azure",
    "upload_to_minio",
]
