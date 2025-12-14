# analyzer.py
import requests


class RepoAnalysisError(ValueError):
    """Raised when repository analysis cannot be completed."""


def analyze_repo(repo_url):
    repo_url = repo_url.strip().rstrip("/")
    if "github.com/" not in repo_url:
        raise RepoAnalysisError("Provide a valid GitHub repo URL like https://github.com/owner/repo")

    # Split out owner/repo safely
    parts = repo_url.split("github.com/")[-1].split("/")
    if len(parts) < 2 or not parts[0] or not parts[1]:
        raise RepoAnalysisError("Repository URL should include both owner and repo name")

    owner, repo = parts[0], parts[1]
    api = f"https://api.github.com/repos/{owner}/{repo}"

    def _fetch(url):
        try:
            resp = requests.get(url, timeout=10)
        except requests.RequestException as exc:
            raise RepoAnalysisError(f"Network error contacting GitHub: {exc}") from exc
        if resp.status_code >= 400:
            raise RepoAnalysisError(f"GitHub API error {resp.status_code}: {resp.text[:200]}")
        return resp.json()

    repo_data = _fetch(api)
    contents_resp = _fetch(api + "/contents")
    commits_resp = _fetch(api + "/commits")
    languages = _fetch(api + "/languages")

    contents = contents_resp if isinstance(contents_resp, list) else []
    commits = commits_resp if isinstance(commits_resp, list) else []

    files = [item.get("name", "") for item in contents if isinstance(item, dict)]

    return {
        "name": repo,
        "languages": list(languages.keys()),
        "file_count": len(files),
        "has_readme": "README.md" in files,
        "has_tests": any("test" in f.lower() for f in files),
        "commit_count": len(commits),
    }
