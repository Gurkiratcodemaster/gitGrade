# roadmap.py
import os
from mistralai import Mistral

def generate_ai_feedback(score, repo_data, improvements):
    client = Mistral(
        api_key=os.getenv("MISTRAL_API_KEY")
    )

    prompt = f"""
You are a senior software engineer and mentor.

Evaluate the following GitHub repository using these signals:

Score: {score}/100
Repository data: {repo_data}
Missing / weak areas: {improvements}

Your task:
1. Write a concise professional evaluation summary
2. Generate a personalized improvement roadmap
3. Explain briefly why each improvement matters

Tone:
- Honest
- Mentor-like
- Recruiter-friendly

Use bullet points.
"""

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=400
    )

    return response.choices[0].message.content
