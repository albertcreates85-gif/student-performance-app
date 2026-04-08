import streamlit as st
import numpy as np
import pickle

# Load model

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model.pkl')

print("Looking for model at:", model_path)

model = pickle.load(open(model_path, 'rb'))

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# ---- CUSTOM CSS (PURPLE THEME) ----
st.markdown("""
    <style>
    body {
        background-color: #0e0e1a;
        color: white;
    }
    .main {
        background: linear-gradient(135deg, #1a0033, #330066);
        padding: 20px;
        border-radius: 15px;
    }
    h1 {
        color: #c084fc;
        text-align: center;
    }
    .stButton>button {
        background-color: #7c3aed;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #a855f7;
        color: white;
    }
    .result-pass {
        color: #4ade80;
        font-size: 22px;
        text-align: center;
        font-weight: bold;
    }
    .result-fail {
        color: #f87171;
        font-size: 22px;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.markdown("<h1>🎓 Student Performance Predictor</h1>", unsafe_allow_html=True)
st.write("### 🔮 Predict whether a student will PASS or STRUGGLE")

# ---- INPUT SECTION ----
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        studytime = st.slider("📚 Study Time (1–4)", 1, 4)
        failures = st.slider("❌ Past Failures", 0, 4)

    with col2:
        absences = st.slider("🚫 Absences", 0, 50)
        higher = st.selectbox("🎯 Wants Higher Education?", ["Yes", "No"])

# Convert input
higher_yes = 1 if higher == "Yes" else 0

# ---- PREDICTION ----
if st.button("🚀 Predict Performance"):
    input_data = np.array([[studytime, failures, absences, higher_yes]])
    
    prediction = model.predict(input_data)

    st.markdown("---")

    if prediction[0] == 1:
        st.markdown('<p class="result-pass">✅ Student is likely to PASS</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="result-fail">❌ Student may STRUGGLE</p>', unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("---")
st.caption("Built with ❤️ using Machine Learning")