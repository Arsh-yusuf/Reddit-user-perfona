import os
import cohere
from dotenv import load_dotenv
from utils import extract_username, fetch_user_data
from persona_formatter import format_persona

load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

def build_prompt(posts, comments):
    data = "POSTS:\n"
    for post in posts:
        data += f"- {post['title']}: {post['selftext'][:200]}... [Source]({post['url']})\n"

    data += "\nCOMMENTS:\n"
    for comment in comments:
        data += f"- {comment['body'][:200]}... [Source]({comment['url']})\n"

    return f"""
You are a highly structured Reddit user persona generation AI. Given the following Reddit posts and comments from a user, build a detailed persona. You MUST provide citations in markdown format for each section.

Your output must include these sections. Each must have:
- A short summary or insight
- A citation: either a quote or [Source](https://reddit.com/...)

🧠 Sections to include:

1. NAME (if deduced)
2. AGE — estimate with supporting post or comment
3. OCCUPATION — inferred from context
4. STATUS — e.g., single, married, divorced
5. LOCATION — city or country
6. USER TIER — Lurker, Regular, Power User
7. ARCHETYPE — Thinker, Entertainer, etc.

💡 Traits
List traits like:
- Practical
- Spontaneous
- Analytical
Each must have a supporting quote or [Source](...)

🎯 MOTIVATIONS
Each motivation (e.g., Speed, Comfort) must have a cited example.

🧩 BEHAVIOUR & HABITS
Describe behavior patterns with Reddit comment or post links.

💢 FRUSTRATIONS
List known problems or complaints with post links.

🏁 GOALS & NEEDS
What does the user want to achieve?

🧬 PERSONALITY SCALE
Show a 4-axis chart:
- Introvert ↔ Extrovert
- Thinking ↔ Feeling
- Judging ↔ Perceiving
- Sensing ↔ Intuition
Each scale point must be supported by one example.

💬 USER QUOTE
End with a quote that best captures the user's personality. Add the Reddit [Source](...) for it.

⚠️ RULE:
- If a section has no clear evidence, you MUST say: "No evidence found."
- Never skip a section even if evidence is missing.

--- BEGIN REDDIT DATA ---

{data}

--- END REDDIT DATA ---
"""


def generate_persona(prompt):
    print("Generating persona using Cohere...")
    response = co.chat(
        model="command-r",  # or use "command-r-plus" if available
        message=prompt,
        temperature=0.7,
        max_tokens=1500
    )
    return response.text

def save_output(username, content):
    filename = f"user_persona_{username}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✔] Saved to {filename}")

def main():
    profile_url = input("Enter Reddit user profile URL: ").strip()
    username = extract_username(profile_url)
    posts, comments = fetch_user_data(username)
    prompt = build_prompt(posts, comments)
    persona = generate_persona(prompt)
    formatted = format_persona(username, persona)
    save_output(username, formatted)

if __name__ == "__main__":
    main()
