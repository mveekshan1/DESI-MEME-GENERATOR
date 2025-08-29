# app.py
import streamlit as st
from ai_module import detect_language, translate_caption, get_caption_labels
from meme_fetcher import fetch_meme_image
from PIL import ImageDraw, ImageFont
import io
import textwrap

# ---------------------------
# App Configuration
# ---------------------------
st.set_page_config(
    page_title="🎭 Desi Meme Generator",
    page_icon="🎭",
    layout="centered"
)

# ---------------------------
# Sidebar Settings
# ---------------------------
with st.sidebar:
    st.header("⚙️ Meme Settings")
    font_size = st.slider("Font Size", min_value=20, max_value=60, value=28)
    font_color = st.color_picker("Font Color", "#FFFFFF")
    st.markdown("---")
    st.info("💡 Enter text in any language. The app will auto-detect, translate, and generate a meme!")

# ---------------------------
# Main App UI
# ---------------------------
st.title("🎭 Desi Meme Generator")
st.markdown(
    "Enter any funny line in **any language** and get a meme instantly!"
)

# Unique input key
user_input = st.text_input("👉 Enter your meme prompt", key="meme_prompt")

if user_input:
    try:
        # 1️⃣ Detect language
        lang = detect_language(user_input)
        st.write(f"🗣 **Detected Language:** {lang}")

        # 2️⃣ Translate if not English
        english_prompt = translate_caption(user_input) if lang != 'en' else user_input
        st.write(f"🔤 **Translated Prompt:** {english_prompt}")

        # 3️⃣ Get meme categories
        labels = get_caption_labels(english_prompt)

        # 4️⃣ Try multiple labels to fetch meme
        meme_image = None
        for label in labels:
            meme_image = fetch_meme_image(label)
            if meme_image:
                break

        if meme_image:
            # ---------------------------
            # Overlay Text on Meme
            # ---------------------------
            draw = ImageDraw.Draw(meme_image)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()

            # Wrap text to fit meme width
            max_width = meme_image.width - 20
            lines = textwrap.wrap(user_input.upper(), width=30)
            y_text = 10
            for line in lines:
                w, h = draw.textsize(line, font=font)
                x_text = (meme_image.width - w) / 2  # center align
                draw.text((x_text, y_text), line, font=font, fill=font_color, stroke_width=1, stroke_fill="black")
                y_text += h + 5

            # ---------------------------
            # Display Meme
            # ---------------------------
            st.image(meme_image, caption="😂 Your Generated Meme", use_container_width=True)

            # ---------------------------
            # Download Button
            # ---------------------------
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
