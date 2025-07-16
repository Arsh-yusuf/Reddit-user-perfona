import praw
import os
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="user_persona_builder"
)

def extract_username(profile_url):
    return profile_url.rstrip('/').split('/')[-1]

def fetch_user_data(username, limit=50):
    user = reddit.redditor(username)
    posts, comments = [], []

    for post in tqdm(user.submissions.new(limit=limit), desc="Fetching posts"):
        posts.append({
            "title": post.title,
            "selftext": post.selftext,
            "url": f"https://reddit.com{post.permalink}"
        })

    for comment in tqdm(user.comments.new(limit=limit), desc="Fetching comments"):
        comments.append({
            "body": comment.body,
            "url": f"https://reddit.com{comment.permalink}"
        })

    return posts, comments
