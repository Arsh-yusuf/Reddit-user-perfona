### 🧠 Reddit User Persona Generator

This Python tool extracts posts and comments from any Reddit user, analyzes them using Cohere's AI, and generates a structured User Persona complete with citations to the Reddit sources used.

🧾 Example persona: Name, Age, Occupation, Location, Traits, Goals, Frustrations, Behavior, and more — each supported by quotes or post links.

### 📁 Project Structure

        reddit_user_persona/
        ├── .env                     # Store your API keys
        ├── main.py                 # Main script to run
        ├── utils.py                # Reddit scraping logic
        ├── persona_formatter.py    # Formats output as structured persona
        ├── requirements.txt        # Install dependencies
        └── README.md               # This file


### 🔧 Setup Instructions
✅ 1. Clone the Repo or Download Code
        git clone https://github.com/yourusername/reddit-user-persona.git
        cd reddit-user-persona

✅ 2. Install Required Libraries
Make sure you're using Python 3.8+. Then install dependencies:
        pip install -r requirements.txt

✅ 3. Get Your API Keys
🔹 Reddit API (for scraping)
    Visit: https://www.reddit.com/prefs/apps

    Click “Create another app…”

    App Type: script

    Name: anything (e.g., personaBot)

    Redirect URI: http://localhost:8080

    After saving:

    client_id = string under the app name

    client_secret = "secret" value shown below

    🔹 Cohere API (for LLM)
    Visit: https://dashboard.cohere.com/api-keys

    Copy the key (you’ll use it in .env)

### ✅ 4. Add Keys to .env File
Create a .env file in your root directory:

    REDDIT_CLIENT_ID=your_reddit_client_id
    REDDIT_CLIENT_SECRET=your_reddit_client_secret
    COHERE_API_KEY=your_cohere_api_key

🚀 How to Run the Script
    Run the main script using:

    python main.py

🔹 You’ll be prompted:
    Enter Reddit user profile URL:
    Example:
    https://www.reddit.com/user/Hungry-Move-6603/

    The script will:

    Scrape 50 posts & comments from that user

    Send the content to Cohere

    Generate a full persona

    Save output to a .txt file like user_persona_Hungry-Move-6603.txt
