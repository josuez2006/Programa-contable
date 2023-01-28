import fitz

def pdf_to_text_convert(file_path: str) -> str:
    text = ''

    DIGITIZED_FILE = file_path
    SCANNED_FILE = file_path


    with fitz.open(DIGITIZED_FILE) as doc:
        for page in doc:
            text = text + page.get_text()


    return text
