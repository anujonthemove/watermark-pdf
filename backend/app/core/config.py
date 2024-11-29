import os

class Config:
    UPLOADS_DIR = os.getenv("UPLOAD_DIR", "uploads")
    DOWNLOADS_DIR = os.getenv("DOWNLOAD_DIR", "downloads")
    WATERMARKS_DIR = os.getenv("WATERMARK_DIR", "watermarks")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    
    MINIO_HOST = os.getenv("MINIO_HOST", "localhost")
    MINIO_PORT = os.getenv("MINIO_PORT", "9000")
    MINIO_ENDPOINT = f"{MINIO_HOST}:{MINIO_PORT}"
    MINIO_ACCESS_KEY = os.getenv("MINIO_ROOT_USER")
    MINIO_SECRET_KEY = os.getenv("MINIO_ROOT_PASSWORD")
    MINIO_BUCKET = os.getenv("MINIO_BUCKET", "watermarkpdf")
    MINIO_UPLOADS_PREFIX = os.getenv("MINIO_UPLOADS_PREFIX", "uploads/")
    MINIO_DOWNLOADS_PREFIX = os.getenv("MINIO_DOWNLOADS_PREFIX", "downloads/")
    MINIO_WATERMARKS_PREFIX = os.getenv("MINIO_WATERMARKS_PREFIX", "watermarks/")