# job-match-resume
A semantic matching tool that compares job descriptions and resumes using transformer models like MiniLM.

# Resume
1. Upload your resume.
2. Parse the data with PyMuPDF or pdfplumber.

# Job Description
1. Upload a plain-text of job description.
2. Parse data.

# Cleaning & Preprocessing
1. Tokenization, lemmatization, stopwords removel.
2. Using nltk and spacy.

# Keyword Extraction
1. Use TF-IDF or RAKE to extract all/top skills/keywords.

# Similarity Score
1. Use cosine_similarity() from sklearn to compare resume and job description.
2. Display the % of match.
3. Display missing skills.

# TECH STACK
Python, StreamLit, scikit-learn, spacy, nltk, pdfplumber, etc (confirm later)

# Features
- Semantic similarity using Sentence Transformers
- Resume and job description input APIs
- Built with FastAPI and Python
- Extensible for real-time matching and explanations

## Setup
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

# TODO
- Add frontend.
- Improve Match Explanation.
- Dockerize
