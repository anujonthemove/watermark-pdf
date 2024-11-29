import boto3
from botocore.exceptions import ClientError
from app.core.config import Config

s3_client = boto3.client(
    "s3",
    endpoint_url=f"http://{Config.MINIO_ENDPOINT}",
    aws_access_key_id=Config.MINIO_ACCESS_KEY,
    aws_secret_access_key=Config.MINIO_SECRET_KEY,
)

def upload_file_to_minio(file_path: str, object_name: str) -> str:
    """
    Uploads a file to MinIO.
    
    Args:
        file_path (str): Local file path.
        object_name (str): Path in MinIO bucket (e.g., 'uploads/file.pdf').

    Returns:
        str: URL to the uploaded file.
    """
    try:
        s3_client.upload_file(file_path, Config.MINIO_BUCKET, object_name)
        # return f"http://{Config.MINIO_ENDPOINT}/{Config.MINIO_BUCKET}/{object_name}"
    except ClientError as e:
        raise RuntimeError(f"Failed to upload file to MinIO: {e}")

def download_file_from_minio(object_name: str, download_path: str):
    """
    Downloads a file from MinIO.

    Args:
        object_name (str): Path in MinIO bucket (e.g., 'downloads/file.pdf').
        download_path (str): Local file path to save the downloaded file.
    """
    try:
        s3_client.download_file(Config.MINIO_BUCKET, object_name, download_path)
    except ClientError as e:
        raise RuntimeError(f"Failed to download file from MinIO: {e}")
