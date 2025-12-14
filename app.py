# app.py
from analyzer import analyze_repo
from scorer import score_repo
from roadmap import generate_ai_feedback

repo_url = input("Enter GitHub Repository URL: ")

data = analyze_repo(repo_url)
score, improvements = score_repo(data)

print("\n===== GitGrade Result =====")
print(f"Score: {score}/100\n")

ai_output = generate_ai_feedback(score, data, improvements)
print("AI Evaluation & Roadmap:\n")
print(ai_output)
