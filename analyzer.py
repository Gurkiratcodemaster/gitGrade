# analyzer.py
import requests

def analyze_repo(repo_url):
    owner, repo = repo_url.replace("https://github.com/", "").split("/")
    api = f"https://api.github.com/repos/{owner}/{repo}"

    repo_data = requests.get(api).json()
    contents_resp = requests.get(api + "/contents").json()
    commits_resp = requests.get(api + "/commits").json()
    languages = requests.get(api + "/languages").json()

    # Handle API responses safely
    contents = contents_resp if isinstance(contents_resp, list) else []
    commits = commits_resp if isinstance(commits_resp, list) else []
    
    files = [item["name"] for item in contents if isinstance(item, dict)]

    return {
        "name": repo,
        "languages": list(languages.keys()),
        "file_count": len(files),
        "has_readme": "README.md" in files,
        "has_tests": any("test" in f.lower() for f in files),
        "commit_count": len(commits),
    }
