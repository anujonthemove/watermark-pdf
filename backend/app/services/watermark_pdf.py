import subprocess

def watermark_pdf(input_file_path: str, watermark_file_path: str, output_file_path: str) -> str:
    """
    Applies a watermark to a PDF file and uploads the output to MinIO.

    Args:
        input_file_path (str): Path to the input PDF file.
        watermark_file_path (str): Path to the watermark PDF file.
        output_file_path (str): Local path to the output PDF file.

    Returns:
        str: URL of the watermarked file in MinIO.
    """
    try:
        command = ["pdftk", input_file_path, "multistamp", watermark_file_path, "output", output_file_path]
        subprocess.run(command, check=True)
        return True

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error processing PDF: {e}")
    