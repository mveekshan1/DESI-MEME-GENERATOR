# ai_module.py

from langdetect import detect, DetectorFactory
from deep_translator import GoogleTranslator
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
        lang = detect(text)
        return lang
    except:
        return "en"  # fallback to English

# -------------------------------
# 2️⃣ Translation Function
# -------------------------------
def translate_caption(text):
    """
    Translates any text to English using Deep Translator.
    Returns the original text if translation fails.
    """
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
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
        return ["funny"]  # fallback
