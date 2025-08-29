import streamlit as st
from ai_module import detect_language, translate_caption, get_caption_labels
from meme_fetcher import fetch_meme_image
from PIL import ImageDraw, ImageFont
import io

# Streamlit page configuration
st.set_page_config(page_title="Desi Meme Generator", layout="centered")

# Title & description
st.title("🎭 Desi Meme Generator")
st.markdown("Enter any funny line in **any language** and get a meme!")

# User input
user_input = st.text_input("Enter your meme prompt (e.g., 'Erra tinnava')")

if user_input:
    # Detect language
    lang = detect_language(user_input)
    st.write(f"🗣 Detected Language: {lang}")

    # Translate if not English
    english_prompt = translate_caption(user_input) if lang != 'en' else user_input
    st.write(f"🔤 Translated Prompt: {english_prompt}")

    # Get caption label
    labels = get_caption_labels(english_prompt)
    meme_image = fetch_meme_image(labels)

    if meme_image:
        # Add user text overlay on meme
        draw = ImageDraw.Draw(meme_image)
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except IOError:
            font = ImageFont.load_default()
        text = user_input.upper()
        draw.text((10, 10), text, font=font, fill="white")

        # Display meme
        st.image(meme_image, caption="Generated Meme", use_container_width=True)

        # Download button
        buffer = io.BytesIO()
        meme_image.save(buffer, format="PNG")
        st.download_button(
            label="📥 Download Meme",
            data=buffer.getvalue(),
            file_name="desi_meme.png",
            mime="image/png"
        )
    else:
        st.warning("Couldn't find a suitable meme image.")
