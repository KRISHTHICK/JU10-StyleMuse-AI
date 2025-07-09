# app.py – StyleMuse AI: Personalized Fashion Style Curator

import streamlit as st
import ollama

# --- User Profile Input ---
def get_user_profile():
    with st.form("profile_form"):
        col1, col2 = st.columns(2)
        with col1:
            height = st.selectbox("Height Range", ["<5ft", "5ft–5.5ft", "5.6ft–6ft", ">6ft"])
            body_type = st.selectbox("Body Type", ["Hourglass", "Pear-shaped", "Apple-shaped", "Rectangle"])
        with col2:
            skin_tone = st.selectbox("Skin Tone", ["Fair", "Medium warm", "Olive", "Tan", "Dark"])
            personality = st.selectbox("Style Personality", ["Classic", "Trendy", "Minimalist", "Boho", "Bold"])

        occasion = st.selectbox("Occasion", ["Daily Casual", "Date Night", "Wedding Guest", "Work/Formal", "Party"])
        submitted = st.form_submit_button("Generate My Style ✨")

    if submitted:
        return {
            "height": height,
            "body_type": body_type,
            "skin_tone": skin_tone,
            "personality": personality,
            "occasion": occasion
        }
    return None

# --- LLM Prompt Generation ---
def build_fashion_prompt(profile):
    prompt = f"""
You are a virtual fashion stylist. Based on this user profile:

Height: {profile['height']}
Body Type: {profile['body_type']}
Skin Tone: {profile['skin_tone']}
Style Personality: {profile['personality']}
Occasion: {profile['occasion']}

Give the following:
1. One personalized outfit recommendation
2. 3 colors that best suit them
3. 3 fashion tips (do's and don'ts)
Return result in JSON.
"""
    return prompt

# --- Query LLaMA via Ollama ---
def query_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Streamlit UI ---
st.set_page_config(page_title="StyleMuse AI", layout="centered")
st.title("👗 StyleMuse AI – Your Personal Fashion Stylist")
st.markdown("_Get tailored outfit ideas based on your style, body, and occasion._")

profile = get_user_profile()
if profile:
    with st.spinner("Styling your outfit..."):
        prompt = build_fashion_prompt(profile)
        result = query_llm(prompt)
        st.markdown("### 💃 Your Personalized Style Suggestion")
        st.code(result, language="json")
