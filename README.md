# Desi Meme Generator 🇮🇳

An open-source, AI-powered **Streamlit application** that empowers users to create and share memes in their local Indian languages.  

Built as part of the **Summer of AI 2025 Internship (Swecha)**, this project bridges **fun meme culture** with **linguistic diversity** by enabling meme creation in multiple Indian languages while also helping build an **open-source informal language corpus**.

---

## 🚀 Features

- 🎭 **Cultural Meme Templates**: Bollywood, Tollywood, Cricket, Politics & more
- 🗣️ **Multilingual Captions**: Add memes in **regional Indian languages**
- 🤖 **AI-powered Caption Suggestions**: Get smart, context-aware captions
- 🔄 **Translation Support**: Translate captions across Indian languages (via open-source models)
- 📦 **Corpus Collection**: Captures informal, slang-rich user-generated text
- 🌐 **Offline-first Mode**: Works smoothly in low-bandwidth environments
- 💾 **Data Storage**: Saves memes + captions securely for corpus building

---

## 🧠 AI Component

We integrated open-source **NLP models**:
- **Hugging Face Transformers** → for text generation
- **IndicTrans / AI4Bharat models** → for multilingual translation
- **Caption Suggestion Engine** → recommends meme text based on template + language

---

## 📦 Tech Stack

- **Frontend/UI** → Streamlit  
- **Backend** → Python (FastAPI/Streamlit APIs)  
- **AI/ML** → Hugging Face Transformers, IndicTrans  
- **Deployment** → Hugging Face Spaces / Streamlit Cloud  
- **Version Control** → GitHub / Code.Swecha  
- **Languages Supported** → Hindi, Telugu, Tamil, Kannada, Malayalam, Bengali, Marathi, and English  

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/mveekshan1/DESI-MEME-GENERATOR.git
cd DESI-MEME-GENERATOR

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
