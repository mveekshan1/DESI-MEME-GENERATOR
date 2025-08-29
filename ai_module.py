from langdetect import detect
from googletrans import Translator
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def detect_language(text):
    return detect(text)

def translate_caption(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    return translation.text

def get_caption_labels(prompt):
    labels = ["funny", "sarcastic", "angry", "romantic", "movie", "cringe", "friend", "food", "dialogue"]
    result = classifier(prompt, candidate_labels=labels)
    return result["labels"][0]
from langdetect import detect
from googletrans import Translator
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def detect_language(text):
    return detect(text)

def translate_caption(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    return translation.text

def get_caption_labels(prompt):
    labels = ["funny", "sarcastic", "angry", "romantic", "movie", "cringe", "friend", "food", "dialogue"]
    result = classifier(prompt, candidate_labels=labels)
    return result["labels"][0]

