# JU10-StyleMuse-AI
GEN AI

 StyleMuse AI – Personalized Outfit & Fashion Style Curator
👗 What It Does
StyleMuse AI acts like a virtual fashion stylist and trend advisor that:

Understands your body type, skin tone, personality, and preferences

Curates outfits and color palettes that suit your style

Recommends daily/occasion-based looks from online fashion collections

Provides fashion do’s and don’ts tailored to you

Can even generate AI-based outfit mockups

💎 Key Features
Feature	Description
🧍 User Profile Builder	Enter height, skin tone, body shape, and preferred styles
🎯 Occasion Selector	Choose the event: casual, date, wedding, formal, etc.
👕 Outfit Generator (LLM)	Personalized fashion advice and outfit recommendations
🎨 Color Palette Matcher	Suggests best-fit colors for your tone
🧠 Style Tips	AI-powered do’s and don’ts, what to avoid
📸 Optional: Upload photo	Analyze and match clothing style using computer vision

🧑‍💻 Tech Stack
Layer	Tool
UI	Streamlit
LLM	Ollama (LLaMA3) or GPT
Color Matching	Custom logic + colormath
Vision (optional)	OpenCV + CLIP for image-based recommendations
Data Source	OpenFashion APIs, dummy data, or scraped catalogs

# 👗 StyleMuse AI – Personalized Fashion Stylist

StyleMuse AI is a virtual fashion stylist powered by LLMs. Based on user inputs like body type, skin tone, and style preference, it recommends tailored outfits, color palettes, and styling tips.

---

## 💡 Features

- Personalized outfit ideas for various occasions
- Color suggestions based on skin tone
- Fashion do’s and don’ts
- Uses LLaMA (via Ollama) for natural style recommendations

---

## 🧪 Inputs

- Height
- Body Type
- Skin Tone
- Style Personality
- Occasion (e.g., date, formal, party)

---

## 🚀 Setup

```bash
git clone https://github.com/yourusername/stylemuse-ai.git
cd stylemuse-ai
pip install -r requirements.txt
ollama pull llama3
streamlit run app.py
