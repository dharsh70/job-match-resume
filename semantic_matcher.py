# semantic_matcher.py
from sentence_transformers import SentenceTransformer, util
from text_preprocessing import preprocess_text

# Load once
model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_match(resume_text: str, jd_text: str) -> float:
    resume_text = preprocess_text(resume_text)
    jd_text = preprocess_text(jd_text)

    embeddings = model.encode([resume_text, jd_text], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    
    return float(similarity.item()) * 100  # Return score as percentage
