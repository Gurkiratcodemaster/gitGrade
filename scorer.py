# scorer.py
def score_repo(data):
    score = 0
    feedback = []

    if data["has_readme"]:
        score += 20
    else:
        feedback.append("Add a clear README with setup instructions")

    if data["has_tests"]:
        score += 20
    else:
        feedback.append("Add unit or integration tests")

    if data["commit_count"] >= 20:
        score += 20
    else:
        feedback.append("Commit more frequently with meaningful messages")

    if data["file_count"] >= 5:
        score += 20
    else:
        feedback.append("Improve project structure")

    if len(data["languages"]) >= 1:
        score += 20

    return score, feedback
