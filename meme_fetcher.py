import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import random
import os

# -------------------------------
# 1️⃣ Unsplash API Settings
# -------------------------------
UNSPLASH_ACCESS_KEY = "jzznyrhg27L0U3Z9qzDPvge5VMyGxaQ2ndG0RILZtS8"  # Replace with your key
UNSPLASH_URL = "https://api.unsplash.com/photos/random"

# -------------------------------
# 2️⃣ Local Meme Dataset (Fallback)
# -------------------------------
LOCAL_MEMES_DIR = "memes"  # folder in your project containing meme images
MEME_CATEGORIES = {
    "funny": ["funny1.jpg", "funny2.jpg"],
    "sarcastic": ["sarcastic1.jpg", "sarcastic2.jpg"],
    "romantic": ["romantic1.jpg", "romantic2.jpg"],
    "angry": ["angry1.jpg", "angry2.jpg"],
    # add more categories and images
}

# -------------------------------
# 3️⃣ Fetch Meme Function
# -------------------------------
def fetch_meme_image(label):
    """
    Fetch a meme image based on the label.
    Tries Unsplash API first, falls back to local dataset.
    Returns a PIL Image object or None if all fails.
    """
    # --- Try Unsplash API ---
    if UNSPLASH_ACCESS_KEY:
        try:
            params = {"query": f"{label} meme", "client_id": UNSPLASH_ACCESS_KEY}
            response = requests.get(UNSPLASH_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            image_url = data["urls"]["regular"]
            img_response = requests.get(image_url, timeout=5)
            img_response.raise_for_status()
            return Image.open(BytesIO(img_response.content)).convert("RGB")
        except (requests.RequestException, UnidentifiedImageError, KeyError):
            pass  # Unsplash failed, fallback to local

    # --- Fallback to local dataset ---
    files = MEME_CATEGORIES.get(label.lower(), [])
    for file_name in files:
        file_path = os.path.join(LOCAL_MEMES_DIR, file_name)
        if os.path.exists(file_path):
            try:
                return Image.open(file_path).convert("RGB")
            except UnidentifiedImageError:
                continue

    # --- If all fails ---
    return None
