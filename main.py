from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from analyzer import analyze_repo
from scorer import score_repo
from roadmap import generate_ai_feedback

app = FastAPI(title="GitGrade – AI GitHub Evaluator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RepoRequest(BaseModel):
    repo_url: str

@app.post("/analyze")
def analyze_repository(data: RepoRequest):
    repo_data = analyze_repo(data.repo_url)
    score, improvements = score_repo(repo_data)
    ai_feedback = generate_ai_feedback(score, repo_data, improvements)

    return {
        "score": score,
        "repo_data": repo_data,
        "ai_feedback": ai_feedback
    }
