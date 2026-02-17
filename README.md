🚀 What is Streamlit?
Streamlit is a Python framework used to build interactive web applications easily — especially for:
Data science projects
Machine learning apps
Dashboards
Mini tools (like your Quiz Game)

The best part?
👉 You only write Python code — no need for HTML, CSS, or JavaScript.

📌 Why Streamlit is Popular?
Simple and beginner-friendly
Converts Python script into web app
Very fast development
Great for ML & AI projects
Auto refresh on changes

Basic Streamlit Structure
Here is the simplest Streamlit program:

import streamlit as st
st.title("Hello Jeevi 👋")
st.write("Welcome to Streamlit!")

Run using:
streamlit run filename.py
It automatically opens in browser 🌐

🛠️ Important Streamlit Functions
1️⃣ Text Display
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.write("Normal text")
st.markdown("**Bold Text**")

2️⃣ User Input
name = st.text_input("Enter your name")
age = st.number_input("Enter age")
choice = st.selectbox("Choose option", ["A", "B", "C"])

3️⃣ Buttons
if st.button("Click Me"):
    st.write("Button clicked!")

4️⃣ Radio Buttons (Used in Your Quiz)
option = st.radio("Choose one", ["Option 1", "Option 2"])

5️⃣ Session State (Very Important 🔥)
Used to store values between refresh.

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increase"):
    st.session_state.count += 1
st.write(st.session_state.count)
Without session state → values reset every refresh.

🎯 Where Streamlit is Used?
ML Model Deployment
AI Projects
Data Dashboards
Portfolio Projects
Internal Company Tools
College Mini Projects

💡 In Simple Words
Streamlit =
"Python code → instantly becomes website"

Since you are learning:
Python
AI
Web Development
Streamlit is PERFECT because:
No need to learn backend
Easy deployment
Good for ML + Projects
Good resume project builder
