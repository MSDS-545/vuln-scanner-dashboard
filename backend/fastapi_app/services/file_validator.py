ALLOWED_TYPES = [".py"]

def validate_file(filename):

    if not any(filename.endswith(x) for x in ALLOWED_TYPES):
        raise ValueError("Invalid file type")