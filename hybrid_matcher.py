# hybrid_matcher.py
from resume_parser import extract_text_from_pdf
from jd_parser import extract_text_from_txt
from text_preprocessing import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def hybrid_match_resume_to_jd(resume_path, jd_path, weight_overlap=0.4, weight_tfidf=0.6):
    # Raw text
    resume_text = extract_text_from_pdf(resume_path)
    jd_text = extract_text_from_txt(jd_path)

    # TF-IDF similarity
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    tfidf_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

    # Token overlap
    resume_tokens = set(preprocess_text(resume_text))
    jd_tokens = set(preprocess_text(jd_text))
    matched = resume_tokens & jd_tokens
    overlap_score = (len(matched) / len(jd_tokens)) * 100 if jd_tokens else 0

    # Combined score
    combined_score = (weight_overlap * overlap_score) + (weight_tfidf * tfidf_score)

    return {
        "tfidf_score": round(tfidf_score, 2),
        "overlap_score": round(overlap_score, 2),
        "combined_score": round(combined_score, 2),
        "matched_keywords": list(matched),
        "missing_keywords": list(jd_tokens - resume_tokens)
    }
