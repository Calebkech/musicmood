from PIL import Image
import os

def is_audio_file(file):
    """
    Check if the uploaded file is an audio file.
    """
    allowed_extensions = {'mp3', 'wav', 'aac', 'flac'}
    file_ext = file.filename.rsplit('.', 1)[1].lower()
    return '.' in file.filename and file_ext in allowed_extensions

def is_image_file(file):
    """
    Check if the uploaded file is an image file.
    """
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    file_ext = file.filename.rsplit('.', 1)[1].lower()
    return '.' in file.filename and file_ext in allowed_extensions

def compress_image(image_path, output_path, quality=75):
    """
    Compress the image to save server storage.
    """
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        img.save(output_path, "JPEG", optimize=True, quality=quality)
        print(f"Image compressed and saved to: {output_path}")
    except Exception as e:
        raise Exception(f"Could not compress image: {e}")
