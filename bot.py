
import tweepy
import os
import random
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# Authenticate to X (Twitter) via API v2 Client
client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

EMOJI_LIST = [
    "🤖", "👾", "🚀", "🌙", "⭐", "🔥", "💿", "💾", "📡", "🔋",
    "🕹️", "🖥️", "⚡", "🕶️", "🦾", "🌌", "🧬", "🧪", "🧿", "💎"
]

def post_emoji():
    try:
        emoji = random.choice(EMOJI_LIST)
        response = client.create_tweet(text=emoji)
        print(f"✅ Posted: {emoji}")
        print(f"🔗 Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🤖 Emoji Bot Starting...")
    post_emoji()
  
