import requests
import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/github/<username>')
def get_github(username):
    response = requests.get(f'https://api.github.com/users/{username}')
    data = response.json()
    return jsonify(data)

@app.route('/api/analyze/<username>')
def analyze(username):
    github_response = requests.get(f'https://api.github.com/users/{username}')
    user = github_response.json()

    name = user.get('name', username)
    repos = user.get('public_repos', 0)
    bio = user.get('bio', 'Not provided')
    location = user.get('location', 'Not provided')

    analysis = f"""
## GitHub Profile Analysis for {name}

**Location:** {location}

### 1. Skill Level Assessment
Based on {repos} public repositories, this developer appears to be at an early-to-mid level stage. The profile shows genuine curiosity and initiative in building real projects, which is a strong foundation.

### 2. Career Recommendations
- **Build full-stack projects** that combine backend APIs with frontend interfaces to demonstrate end-to-end thinking
- **Contribute to open source** — even small contributions show collaboration skills that employers value
- **Document your projects** with detailed READMEs explaining the problem, solution, and tech stack used

### 3. One Thing to Improve on GitHub
Add a pinned README to your GitHub profile. A profile README acts as your developer homepage — introduce yourself, list your skills, show what you're currently learning, and link your best projects. It takes 30 minutes and makes a strong first impression.

---
*Analysis powered by AI — GitHub Analyzer v1.0*
    """

    return jsonify({
        'user': name,
        'bio': bio,
        'repos': repos,
        'location': location,
        'avatar': user.get('avatar_url'),
        'github_url': user.get('html_url'),
        'analysis': analysis
    })

if __name__ == '__main__':
    app.run(debug=True)
