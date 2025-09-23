import os

def allowed_file(filename: str, allowed_extensions=None) -> bool:
    if allowed_extensions is None:
        allowed_extensions = {"png", "jpg", "jpeg", "gif", "mp3"}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
