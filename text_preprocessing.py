# text_preprocessing.py
import re

def preprocess_text(text: str) -> str:
    """
    Minimal preprocessing: Remove extra spaces, lowercase, and normalize.
    Transformers prefer raw, clean text without aggressive token filtering.
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
