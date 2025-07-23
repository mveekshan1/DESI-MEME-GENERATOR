## 🧑‍🤝‍🧑 1. Team Information

**Team Name:** MemeStream  
**Project Name:** Desi Meme Generator 🇮🇳
**Program:** Summer of AI 2025 – Swecha  
**Team Members:**
- veekshan12 – Team Lead, AI Integration   
- @sakshi08  – Frontend Developer
- Keeru@1911 – Backend Developer  
- Tejasri@18 – Testing & Documentation  
- Shivapriya15 – Outreach & User Growth

---

## 📱 2. Application Overview

**Desi Meme Generator** is an open-source, AI-powered application built using Streamlit that allows users to create and share memes in their native Indian languages. The project is designed to collect informal, culturally rich language data from users across India in a fun, accessible, and low-bandwidth-friendly way.

The application helps users:
- Choose a meme template from a rotating collection (movies, cricket, politics, etc.)
- Add their own caption in **their local dialect or language**
- Generate a final meme image that can be downloaded and shared
- Contribute linguistic and cultural data through their captions

This data becomes part of a **valuable corpus** used to train open-source Indian language models, contributing to projects like **viswam.ai**.

---

## 🧠 3. AI Integration Details

We will use open-source NLP models to:
- (Optional MVP) Suggest captions based on the selected meme image and language
- (Phase 2) Translate user-generated captions into multiple Indian languages using models like **IndicTrans** or **BLOOM**

All models will be integrated using lightweight APIs suitable for low-bandwidth conditions. AI use is minimal in the MVP phase but designed to scale.

---

## 🏗️ 4. Technical Architecture & Development

**Frontend:**  
- Developed using **Streamlit**
- Allows selection of meme templates
- Caption input box with language selector
- Output: Captioned meme image (text + template)

**Backend:**
- Meme templates stored in local/static folder
- Captions and metadata saved in a structured `.csv` or database
- Offline-first: Works without internet and syncs when online

**File Structure:**
app/
templates/ # Meme images
main.py # Streamlit interface 
utils/ # Helper functions
data/ # Collected caption data
requirements.txt
README.md
REPORT.md
LICENSE

## (File structure may differ according to the app)

**Deployment:**  
- Public and no login required

## 🧪 5. User Testing & Feedback

### **Methodology:**
- Recruit testers from WhatsApp, student groups, and rural youth networks
- Ask users to create 1–3 memes in their native language
- Collect feedback on:
  - Usability on mobile/low-bandwidth
  - Ease of meme creation
  - Language support

### **Feedback Tools:**
- Embedded feedback form in app
- Direct WhatsApp feedback from testers
- Google Form survey

### **Bug Log & Fixes:**
A table will be maintained in CHANGELOG.md with:
- Bug description
- User report
- Fix implementation and date

## 🔁 6. Project Lifecycle & Roadmap

### 🟩 Week 1 – Rapid Development Sprint:
- Build core Streamlit app
- Add meme template upload + caption editor
- Generate final meme output
- Deploy on Hugging Face
- Implement offline-first caching

**Deliverables:**  
- Functional MVP deployed publicly  
- Meme generation tested with at least 5 templates

---

### 🟨 Week 2 – Beta Testing & Iteration:

**Plan:**
- Recruit 15–25 testers
- Collect 50–100 meme submissions
- Log feedback and implement UX improvements

**Iteration Plan:**
- Improve UI for mobile
- Add emoji support in captions
- Fix any image-text alignment bugs


### 🟦 Weeks 3–4 – User Acquisition & Corpus Growth Campaign

**Target Audience:**
- Students from Tier 2/3 colleges
- WhatsApp meme groups
- Cultural clubs (e.g., Telugu Sahitya Parishad)
- Meme creators on Instagram

**Growth Channels:**
- Instagram reels
- WhatsApp broadcast messages
- Posters in rural colleges

**Metrics to Track:**
- # of unique users
- # of meme submissions
- Language variety (Telugu, Hindi, Tamil, etc.)
- Feedback collected


### 🟪 Post-Internship Vision & Sustainability

**Planned Features:**
- AI caption suggestions
- Template upload from users
- Language detection

**Corpus Expansion:**
- Partner with meme communities & colleges
- Host meme competitions
- Periodic campaigns for specific themes (e.g., festivals, cricket)

**Sustainability:**
- Maintain open GitHub contributions
- Continue hosting on Hugging Face or integrate with viswam.ai
- Documentation to support community-led growth


## Summary

**Desi Meme Generator 🇮🇳** is more than just a meme tool — it’s a cultural and linguistic corpus engine wrapped in humor. Through fun, creative engagement, we enable data contribution in a way that is inclusive, accessible, and scalable.

We believe this app embodies the **spirit of the Summer of AI 2025** — blending open-source values with grassroots creativity and social impact.
