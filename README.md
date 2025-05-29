# job-match-resume
Input: Resume, Job Description. Output: Skills Match%, Missing Skills

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

# Future Enhancements(if u can/ if you want to)
1. Web scrawl through differnet job postings and suggest jobs to apply to based on resume.
2. Suggest some content to add to resume as a sentence.
