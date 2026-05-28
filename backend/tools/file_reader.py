import pdfplumber
import os

# pdf_locator_path = /Users/willhager/Downloads

def handle_pdf(file_path):
    with pdfplumber.open(file_path) as f:
        full_text = "\n\n".join(page.extract_text() for page in f.pages)
    return full_text

def handle_plaintext(file_path):
    with open(file_path, "r") as f:
        return f.read()

def handle_json(file_path):
    with open(file_path, "r") as f:
        return json.dumps(json.load(f), indent=2)

handlers = {
    ".pdf": handle_pdf,
    ".txt": handle_plaintext,
    ".md": handle_plaintext,
    ".py": handle_plaintext,
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
