import pdfplumber
import os

# pdf_locator_path = /Users/willhager/Downloads

def handle_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        full_text = "\n\n".join(page.extract_text() for page in pdf.pages)
    return full_text

def handle_txt(file_path):
    return None

def handle_md(file_path):
    return None

def handle_py(file_path):
    return None

def handle_json(file_path):
    return None

handlers = {
    ".pdf": handle_pdf,
    ".txt": handle_txt,
    ".md": handle_md,
    ".py": handle_py,
    ".json": handle_json,
}

def file_reader(file_path, query):
    
    ext = os.path.splitext(file_path)[1].lower()
    if ext in handlers:
        handler = handlers[ext]
        content = handler(file_path)
        return content
    else:
        return f"Unsupported file type: {ext}"
