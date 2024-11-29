import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.services.watermark_pdf import watermark_pdf
from app.core.config import Config
from app.utils.file_manager import save_file, cleanup
from app.utils.s3_file_manager import upload_file_to_minio


app = FastAPI()

@app.post("/watermark")
async def apply_watermark(input_pdf_file: UploadFile = File(...), watermark_pdf_file: UploadFile = File(...)):

    try:
        # 1. create folders
        os.makedirs(Config.UPLOADS_DIR, exist_ok=True)
        os.makedirs(Config.DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(Config.WATERMARKS_DIR, exist_ok=True)
        output_file_path = os.path.join(Config.DOWNLOADS_DIR, f"watermarked_{input_pdf_file.filename}")

        # 2. save files locally for processing
        input_pdf = save_file(input_pdf_file, Config.UPLOADS_DIR)
        watermarked_pdf = save_file(watermark_pdf_file, Config.WATERMARKS_DIR)
        status = watermark_pdf(input_pdf, watermarked_pdf, output_file_path)
        if status:
            # upload to minio
            input_s3_path = f"{Config.MINIO_UPLOADS_PREFIX}{input_pdf_file.filename}"
            watermark_s3_path = f"{Config.MINIO_WATERMARKS_PREFIX}{watermark_pdf_file.filename}"
            output_s3_path = f"{Config.MINIO_DOWNLOADS_PREFIX}{os.path.basename(output_file_path)}"

            upload_file_to_minio(input_pdf, input_s3_path)
            upload_file_to_minio(watermarked_pdf, watermark_s3_path)
            upload_file_to_minio(output_file_path, output_s3_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Clean up local files
        cleanup(Config.UPLOADS_DIR)
        cleanup(Config.DOWNLOADS_DIR)
        cleanup(Config.WATERMARKS_DIR)

    return {"message": "Watermark applied successfully", "output_path": output_s3_path}

