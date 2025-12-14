# GitGrade – AI-Powered GitHub Repository Evaluator

## Overview
GitGrade is a web application that automatically evaluates GitHub repositories using explainable rules and AI-generated feedback. Perfect for recruiters, students, and developers who want insights into code quality and project maturity.

## Features
- **Automated Repository Analysis**: Extracts key metrics from any public GitHub repository
- **Intelligent Scoring**: Rates repositories on a 0-100 scale based on:
  - Documentation quality (README presence)
  - Testing practices (test file detection)
  - Development discipline (commit frequency)
  - Project structure (file organization)
  - Technology diversity (language count)
- **AI-Generated Feedback**: Uses Mistral AI to generate personalized improvement roadmaps
- **Web Interface**: Clean, modern UI for easy repository evaluation

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: FastAPI (Python)
- **AI**: Mistral AI API
- **APIs**: GitHub REST API

## Installation

### Prerequisites
- Python 3.8+
- Mistral API Key (get one at [console.mistral.ai](https://console.mistral.ai))

### Setup
1. Clone the repository:
```bash
git clone <repo-url>
cd gitgrade
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file with your Mistral API key:
```
MISTRAL_API_KEY=your_api_key_here
```

## Running the Application

Start the backend server:
```bash
uvicorn main:app --reload --port 8000
```

Open your browser and navigate to:
```
http://localhost:8000
```

Then open `index.html` in your browser or serve it with a simple HTTP server:
```bash
python -m http.server 8080
```

Visit `http://localhost:8080` and paste a GitHub repository URL to analyze.

## Example Usage
1. Paste a GitHub URL: `https://github.com/torvalds/linux`
2. Click "Analyze"
3. Get instant score and personalized improvement suggestions

## Evaluation Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| Documentation | 20 | README.md presence |
| Testing | 20 | Test files detected |
| Commit Discipline | 20 | 20+ commits |
| Project Structure | 20 | 5+ files |
| Technology Diversity | 20 | Multiple languages |

## API Endpoints

### POST `/analyze`
Analyzes a GitHub repository and returns score + AI feedback.

**Request:**
```json
{
  "repo_url": "https://github.com/owner/repo"
}
```

**Response:**
```json
{
  "score": 85,
  "repo_data": { ... },
  "ai_feedback": "Detailed evaluation and roadmap..."
}
```

## Limitations
- Analyzes public repositories only
- No deep code analysis (AST parsing, complexity metrics)
- Rate-limited by GitHub API (60 req/hour for unauthenticated)
- Requires valid Mistral API key for AI feedback

## Future Improvements
- GitHub authentication for higher API rate limits
- Detailed code quality metrics
- CI/CD pipeline detection
- Pull request analysis
- Private repository support
- Dark/Light theme toggle

## Security Notes
- Never commit `.env` file to version control
- Mistral API keys should be kept private
- Use environment variables for sensitive data in production

## License
MIT

## Contributing
Contributions welcome! Please open an issue or submit a pull request.

