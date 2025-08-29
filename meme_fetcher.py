from duckduckgo_search import DDGS
import requests
from PIL import Image
from io import BytesIO

def fetch_meme_image(label):
    with DDGS() as ddgs:
        results = ddgs.images(f"{label} meme", max_results=1)
        image_list = list(results)
        if image_list:
            image_url = image_list[0]["image"]
            response = requests.get(image_url)
            return Image.open(BytesIO(response.content))
    return None

=======
from duckduckgo_search import DDGS
import requests
from PIL import Image
from io import BytesIO

def fetch_meme_image(label):
    with DDGS() as ddgs:
        results = ddgs.images(f"{label} meme", max_results=1)
        image_list = list(results)
        if image_list:
            image_url = image_list[0]["image"]
            response = requests.get(image_url)
            return Image.open(BytesIO(response.content))
    return None
