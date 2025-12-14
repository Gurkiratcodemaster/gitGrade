from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from analyzer import analyze_repo
from scorer import score_repo
from roadmap import generate_ai_feedback
from pathlib import Path

app = FastAPI(title="GitGrade – AI GitHub Evaluator")

# -----------------------------
# CORS (needed if frontend uses fetch)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request model
# -----------------------------
class RepoRequest(BaseModel):
    repo_url: str

# -----------------------------
# FRONTEND ROUTE
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    """
    Serves index.html as the frontend UI
    """
    return Path("index.html").read_text()

# -----------------------------
# API ROUTE
# -----------------------------
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
