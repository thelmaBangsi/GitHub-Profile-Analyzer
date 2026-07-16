import requests
import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

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

    prompt = f"""Analyze this GitHub developer profile and give career advice:

Developer: {name}
Location: {location}
Bio: {bio}
Public Repos: {repos}
GitHub URL: {user.get('html_url')}

Provide:
1. Skill level assessment
2. Career recommendations
3. One thing to improve on GitHub"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return jsonify({
        'user': name,
        'bio': bio,
        'repos': repos,
        'location': location,
        'avatar': user.get('avatar_url'),
        'github_url': user.get('html_url'),
        'analysis': response.text
    })

if __name__ == '__main__':
    app.run(debug=True)
