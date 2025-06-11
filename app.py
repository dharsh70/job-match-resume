# app.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import fitz  # PyMuPDF
from semantic_matcher import semantic_match

app = FastAPI()

def extract_text_from_pdf(file_bytes):
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

@app.post("/match/")
async def match_resume(resume: UploadFile = File(...), jd: UploadFile = File(...)):
    resume_bytes = await resume.read()
    jd_bytes = await jd.read()

    resume_text = extract_text_from_pdf(resume_bytes)
    jd_text = jd_bytes.decode("utf-8")

    match_score = semantic_match(resume_text, jd_text)

    return JSONResponse({
        "match_score": round(match_score, 2)
    })
