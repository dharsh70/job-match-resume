# app_api.py
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')
app = FastAPI()

class MatchRequest(BaseModel):
    resume: str
    job_description: str

@app.post("/match_score")
def match_score(req: MatchRequest):
    resume_emb = model.encode(req.resume, convert_to_tensor=True)
    jd_emb = model.encode(req.job_description, convert_to_tensor=True)
    score = util.pytorch_cos_sim(resume_emb, jd_emb).item()
    return {"semantic_match_score": round(score * 100, 2)}