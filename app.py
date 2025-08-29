import streamlit as st
from ai_module import detect_language, translate_caption, get_caption_labels
from meme_fetcher import fetch_meme_image
from PIL import ImageDraw, ImageFont
import io

# ---------------------------
# App Configuration
# ---------------------------
st.set_page_config(page_title="Desi Meme Generator", layout="centered", page_icon="🎭")

# Sidebar Info
with st.sidebar:
    st.header("⚙️ Settings")
    font_size = st.slider("Font Size", 20, 60, 28, key="font_size")
    font_color = st.color_picker("Font Color", "#FFFFFF", key="font_color")
    st.markdown("---")
    st.info("💡 Enter text in any language. The app will auto-detect and translate.")

# ---------------------------
# Main App UI
# ---------------------------
st.title("🎭 Desi Meme Generator")
st.markdown("Enter any funny line in **any language** and get a meme instantly!")

# Input with unique key
user_input = st.text_input("👉 Enter your meme prompt", key="meme_prompt")

if user_input:
    try:
        # Detect language
        lang = detect_language(user_input)
        st.write(f"🗣 **Detected Language:** {lang}")

        # Translate if not English
        english_prompt = translate_caption(user_input) if lang != 'en' else user_input
        st.write(f"🔤 **Translated Prompt:** {english_prompt}")

        # Get meme category & fetch meme
        labels = get_caption_labels(english_prompt)
        meme_image = fetch_meme_image(labels)

        if meme_image:
            # Add text overlay
            draw = ImageDraw.Draw(meme_image)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()

            text = user_input.upper()
            draw.text((10, 10), text, font=font, fill=font_color)

            # Show final meme
            st.image(meme_image, caption="😂 Your Generated Meme", use_container_width=True)

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
            st.warning("⚠️ Couldn't find a suitable meme image. Try another prompt.")

    except Exception as e:
        st.error(f"🚨 Oops! Something went wrong: {str(e)}")

else:
    st.info("✍️ Enter a meme prompt above to get started!")
