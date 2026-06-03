import re

def parse_python_traceback(text: str) -> dict:
    error_match = re.search(r'^(\w+(?:Error|Exception|Warning)[^:]*): (.+)$', text, re.MULTILINE)
    
    error_type = error_match.group(1).strip() if error_match else "Unknown"
    message = error_match.group(2).strip() if error_match else "Could not parse error message"
    
    file_refs = re.findall(r'File "(.*?)", line (\d+)', text)
    
    return {
        "error_type": error_type,
        "message": message,
        "root_file": file_refs[-1][0] if file_refs else None,
        "root_line": int(file_refs[-1][1]) if file_refs else None,
        "call_depth": len(file_refs)
    }
