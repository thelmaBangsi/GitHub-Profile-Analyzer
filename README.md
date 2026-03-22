#GitHub Profile Analyzer

An AI-powered web application that analyzes any GitHub profile and provides personalized career advice and developer insights.

## Features

- Search any GitHub username instantly
- Display profile photo, bio, location and repository count
- AI-powered career analysis and recommendations
- Clean, responsive dark theme UI
- Real-time data from the GitHub API

##Tech Stack

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript (Fetch API, Async/Await, DOM Manipulation)

**Backend:**
- Python
- Flask
- GitHub REST API

##  How It Works

1. User enters a GitHub username
2. Frontend sends request to Flask backend
3. Backend fetches real data from GitHub API
4. AI analyzes the profile and generates career advice
5. Results displayed in a clean, formatted UI

## How To Run
```bash
# Clone the repository
git clone https://github.com/thelmaBangsi/GitHub-Profile-Analyzer

# Navigate to project folder
cd GitHub-Profile-Analyzer

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask flask-cors requests python-dotenv

# Add your API key to .env file
echo "ANTHROPIC_API_KEY=your-key-here" > .env

# Run the app
python3 app.py
```

Then visit `http://127.0.0.1:5000` in your browser.

## 👩‍💻 Developer

Built by **Thelma Bangsi** — Kigali, Rwanda 🇷🇼
