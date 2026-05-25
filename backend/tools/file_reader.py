import pdfplumber

pdf_locator_path = /Users/willhager/Downloads

def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

