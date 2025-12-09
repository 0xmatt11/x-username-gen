
import tweepy
import os
import random
import time
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# --- CONFIGURATION ---
BASE_NAME = "YourName"  # <--- CHANGE THIS
# ---------------------

# Authenticate via API v1.1 (Required for profile updates)
auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_KEY_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

EMOJI_LIST = [
    "🤖", "👾", "🚀", "🌙", "⭐", "🔥", "💿", "💾", "📡", "🔋",
    "🕹️", "🖥️", "⚡", "🕶️", "🦾", "🌌", "🧬", "🧪", "🧿", "💎"
]

def update_profile_name():
    while True:
        try:
            emoji = random.choice(EMOJI_LIST)
            new_name = f"{BASE_NAME} {emoji}"
            
            api.update_profile(name=new_name)
            print(f"✅ Profile updated: {new_name}")
            
            print("⏳ Waiting 60 seconds...")
            time.sleep(60)

        except tweepy.errors.TooManyRequests:
            print("⚠️ Rate Limit Hit! Sleeping for 15 mins...")
            time.sleep(900)
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    print("🤖 Name Changer Bot Starting...")
    update_profile_name()
  
