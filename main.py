from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from analyzer import analyze_repo, RepoAnalysisError
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
    try:
        repo_data = analyze_repo(data.repo_url)
        score, improvements = score_repo(repo_data)
        ai_feedback = generate_ai_feedback(score, repo_data, improvements)
    except RepoAnalysisError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:  # Catch-all to avoid leaking stack traces
        raise HTTPException(status_code=500, detail=f"Unexpected error: {exc}")

    return {
        "score": score,
        "repo_data": repo_data,
        "ai_feedback": ai_feedback
    }
