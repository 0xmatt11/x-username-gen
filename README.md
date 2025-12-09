# 🤖 Twitter (X) Automation Toolkit

A collection of Python scripts for automating tasks on X (formerly Twitter) using the Tweepy library. This toolkit includes an auto-poster, a dynamic profile name changer, and an offline username generator.

## 📂 Included Scripts

| Script | API Tier Req | Description |
| :--- | :--- | :--- |
| **`bot.py`** | Free / Basic | Posts a random emoji to your timeline using API v2 (`create_tweet`). |
| **`name_bot.py`** | Free / Basic | Updates your **Display Name** every 60 seconds with a random emoji (uses API v1.1). |
| **`name_gen.py`** | **None** (Offline) | Generates creative, tech-themed username ideas and checks validity locally (no API required). |

## ⚙️ Prerequisites

* **Python 3.8+**
* **X Developer Account** with a configured Project & App.
* **"Read and Write" Permissions** enabled in the X Developer Portal.

## 📦 Installation

1.  **Clone the repository** (or download the files):
    ```bash
    git clone [https://github.com/0xmatt11/x-username-gen](https://github.com/yourusername/0xmatt11/x-username-gen)
    cd x-username-gen
    ```

2.  **Install dependencies**:
    ```bash
    pip install tweepy python-dotenv
    ```

## 🔑 Configuration (Security)

**NEVER** hardcode your API keys into the Python scripts. Use a `.env` file to keep them secure.

1.  Create a file named `.env` in the root directory.
2.  Paste your keys from the [X Developer Portal](https://developer.twitter.com/en/portal/dashboard) into the file:

```env
# .env file
API_KEY=your_consumer_key_here
API_KEY_SECRET=your_consumer_secret_here
ACCESS_TOKEN=your_access_token_here
ACCESS_TOKEN_SECRET=your_access_token_secret_here
BEARER_TOKEN=your_bearer_token_here  # Optional, only for Basic Tier lookups
