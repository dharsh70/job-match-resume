def extract_text_from_txt(file):
    with open(file, 'r', encoding='utf-8') as f:
        text=f.read()
    return text.strip()