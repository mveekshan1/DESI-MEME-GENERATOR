# ai_module.py

from langdetect import detect, DetectorFactory
import langid
from googletrans import Translator
from transformers import pipeline

# Make langdetect deterministic
DetectorFactory.seed = 0

# Initialize Hugging Face zero-shot classifier once
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# List of possible meme labels
LABELS = ["funny", "sarcastic", "angry", "romantic", "movie", "cringe", "friend", "food", "dialogue"]

# -------------------------------
# 1️⃣ Language Detection Function
# -------------------------------
def detect_language(text):
    """
    Detects the language of the input text.
    Handles single words, slang, and transliterations.
    """
    try:
        # Primary detection using langdetect
        lang = detect(text)
        return lang
    except:
        # Fallback using langid
        lang, confidence = langid.classify(text)
        return lang

# -------------------------------
# 2️⃣ Translation Function
# -------------------------------
def translate_caption(text):
    """
    Translates any text to English.
    Returns the original text if translation fails.
    """
    try:
        translator = Translator()
        translation = translator.translate(text, dest='en')
        return translation.text
    except Exception as e:
        print("Translation failed:", e)
        return text

# -------------------------------
# 3️⃣ Meme Labeling Function
# -------------------------------
def get_caption_labels(prompt, top_k=3):
    """
    Classifies the input prompt into meme categories.
    Returns top_k labels for better meme search.
    """
    try:
        result = classifier(prompt, candidate_labels=LABELS)
        return result["labels"][:top_k]
    except Exception as e:
        print("Labeling failed:", e)
        # Fallback: return a default label
        return ["funny"]
