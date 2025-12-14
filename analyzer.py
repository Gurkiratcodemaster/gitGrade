# analyzer.py
import requests

def analyze_repo(repo_url):
    owner, repo = repo_url.replace("https://github.com/", "").split("/")
    api = f"https://api.github.com/repos/{owner}/{repo}"

    repo_data = requests.get(api).json()
    contents = requests.get(api + "/contents").json()
    commits = requests.get(api + "/commits").json()
    languages = requests.get(api + "/languages").json()

    files = [item["name"] for item in contents]

    return {
        "name": repo,
        "languages": list(languages.keys()),
        "file_count": len(files),
        "has_readme": "README.md" in files,
        "has_tests": any("test" in f.lower() for f in files),
        "commit_count": len(commits),
    }
