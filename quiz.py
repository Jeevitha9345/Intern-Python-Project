import streamlit as st
import random
import pandas as pd
import os
import time
from datetime import datetime

QUIZ_DURATION = 180  # 3 minutes

st.set_page_config(page_title="Quiz Game", page_icon="🧠")
st.title("🧠 Mini Quiz Game")
st.markdown("Test your knowledge across different domains and subdomains!")

# Ask for name first
name = st.text_input("👤 Enter your name to start the quiz:")
if not name:
    st.warning("Please enter your name to continue.")
    st.stop()

# Start timer after name is entered
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

elapsed = time.time() - st.session_state.start_time
time_left = QUIZ_DURATION - elapsed

# Timer Display
timer_placeholder = st.empty()
if time_left <= 0:
    st.session_state.time_up = True
    timer_placeholder.error("⏰ Time's up! Submitting automatically...")
else:
    st.session_state.time_up = False
    mins = int(time_left // 60)
    secs = int(time_left % 60)
    timer_placeholder.warning(f"⏰ Time Left: {mins:02d}:{secs:02d}")

# Quiz Bank
quiz_bank = {
    "Science": {
    "Biology": [
        {
            "question": "Which organ pumps blood?",
            "options": ["Lungs", "Heart", "Kidneys", "Liver"],
            "answer": "Heart"
        },
        {
            "question": "What gas do plants absorb?",
            "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"],
            "answer": "Carbon Dioxide"
        },
        {
            "question": "What is the powerhouse of the cell?", 
            "options": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"], 
            "answer": "Mitochondria"
        },
        {
            "question": "Which blood cells help fight infection?",
            "options": ["Red blood cells", "White blood cells", "Platelets", "Plasma"], 
            "answer": "White blood cells"
        },
        {
            "question": "Which vitamin is produced when sunlight hits the skin?", 
            "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], 
            "answer": "Vitamin D"
        },
    ],
    "Chemistry": [
        {
            "question": "H2O is the chemical formula for?", 
            "options": ["Oxygen", "Hydrogen", "Water", "Helium"], 
            "answer": "Water"
        },
        {
            "question": "What is the chemical symbol for Sodium?", 
            "options": ["S", "So", "Na", "N"], 
            "answer": "Na"
        },
        {
            "question": "Which acid is found in vinegar?", 
            "options": ["Citric Acid", "Acetic Acid", "Sulfuric Acid", "Hydrochloric Acid"], 
            "answer": "Acetic Acid"
        },
        {
            "question": "What is the pH value of pure water?", 
            "options": ["5", "6", "7", "8"], 
            "answer": "7"
        },
        {
            "question": "Which gas is released during photosynthesis?", 
            "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], 
            "answer": "Oxygen"
        },
    ],
    "Physics": [
        {
            "question": "What is the unit of force?",
            "options": ["Joule", "Newton", "Watt", "Pascal"],
            "answer": "Newton"
        },
        {
            "question": "What is the speed of light?",
            "options":["3x10^8 m/s", "5x10^6 m/s", "1x10^5 m/s", "None"],
            "answer": "3x10^8 m/s"
        },
        {
            "question": "Which instrument measures electric current?",
            "options": ["Voltmeter", "Thermometer", "Ammeter", "Barometer"], 
            "answer": "Ammeter"
        },
        {
            "question": "What is the formula for Ohm's Law?",
            "options": ["V = IR", "P = VI", "E = mc²", "F = ma"], 
            "answer": "V = IR"
        },
        {
            "question": "What type of energy is stored in a stretched rubber band?",
            "options": ["Kinetic", "Thermal", "Potential", "Chemical"],
            "answer": "Potential"
        },
        {
            "question": "What does a convex lens do?",
            "options": ["Diverges light", "Absorbs light", "Converges light", "Blocks light"],
            "answer": "Converges light"
        },
    ]
},
    "Technology": {
    "Programming": [
        {
            "question": "Which language is primarily used for Android app development?",
            "options": ["Kotlin", "Swift", "Python", "C#"],
            "answer": "Kotlin"
        },
        {
            "question": "What does IDE stand for?",
            "options": ["Integrated Development Environment", "Instant Debugging Editor", "Internet Development Extension", "Input Data Engine"],
            "answer": "Integrated Development Environment"
        },
        {
            "question": "Which of these is a statically typed language?",
            "options": ["Python", "JavaScript", "Java", "Ruby"],
            "answer": "Java"
        },
        {
            "question": "What symbol is used for comments in Python?",
            "options": ["//", "/*", "#", "--"],
            "answer": "#"
        },
        {
            "question": "Which of these is not a programming language?",
            "options": ["Python", "Java", "HTML", "C++"],
            "answer": "HTML"
        }
    ],
    "Web Development": [
        {
            "question": "Which HTML tag is used to insert an image?",
            "options": ["<img>", "<image>", "<pic>", "<src>"],
            "answer": "<img>"
        },
        {
            "question": "What does CSS stand for?",
            "options": ["Cascading Style Sheets", "Colorful Style Syntax", "Computer Styling System", "Creative Sheet Structure"],
            "answer": "Cascading Style Sheets"
        },
        {
            "question": "Which of these is a frontend framework?",
            "options": ["Django", "React", "Node.js", "MongoDB"],
            "answer": "React"
        },
        {
            "question": "Which property in CSS is used to change text color?",
            "options": ["font-color", "text-style", "color", "style"],
            "answer": "color"
        },
        {
            "question": "JavaScript is primarily used for?",
            "options": ["Styling", "Database", "Client-side scripting", "Server management"],
            "answer": "Client-side scripting"
        }
    ],
    "Cybersecurity": [
        {
            "question": "Which of the following is a strong password?",
            "options": ["password123", "123456", "MyName2023", "T#r8&kL!z"],
            "answer": "T#r8&kL!z"
        },
        {
            "question": "What type of attack involves overwhelming a server with traffic?",
            "options": ["Phishing", "DDoS", "Trojan", "SQL Injection"],
            "answer": "DDoS"
        },
        {
            "question": "What is the purpose of two-factor authentication?",
            "options": ["To speed up login", "To replace passwords", "To add an extra layer of security", "To encrypt data"],
            "answer": "To add an extra layer of security"
        },
        {
            "question": "Which of these is a secure web protocol?",
            "options": ["HTTP", "FTP", "SMTP", "HTTPS"],
            "answer": "HTTPS"
        },
        {
            "question": "Which of the following can help detect malware?",
            "options": ["Ad blocker", "Firewall", "Antivirus software", "VPN"],
            "answer": "Antivirus software"
        }
    ]
},
    "General Knowledge": {
    "Sports": [
        {
            "question": "Which sport uses a shuttlecock?",
            "options": ["Tennis", "Cricket", "Badminton", "Football"],
            "answer": "Badminton"
        },
        {
            "question": "In which country were the first modern Olympic Games held?",
            "options": ["USA", "France", "Greece", "Italy"],
            "answer": "Greece"
        },
        {
            "question": "How many players are there in a football (soccer) team on the field?",
            "options": ["9", "10", "11", "12"],
            "answer": "11"
        },
        {
            "question": "Which country has won the most FIFA World Cups?",
            "options": ["Germany", "Brazil", "Argentina", "Italy"],
            "answer": "Brazil"
        },
        {
            "question": "What is the national sport of Japan?",
            "options": ["Karate", "Baseball", "Sumo Wrestling", "Judo"],
            "answer": "Sumo Wrestling"
        }
    ],
    "Geography": [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Paris", "Rome", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Which is the largest ocean in the world?",
            "options": ["Atlantic", "Pacific", "Indian", "Arctic"],
            "answer": "Pacific"
        },
        {
            "question": "Mount Everest is located in which mountain range?",
            "options": ["Andes", "Alps", "Rockies", "Himalayas"],
            "answer": "Himalayas"
        },
        {
            "question": "Which continent is the Sahara Desert located in?",
            "options": ["Asia", "Australia", "Africa", "South America"],
            "answer": "Africa"
        },
        {
            "question": "Which country has the most number of time zones?",
            "options": ["USA", "India", "Russia", "France"],
            "answer": "France"
        }
    ]
}
}

domain = st.selectbox("🌐 Choose Domain", list(quiz_bank.keys()))
subdomain = st.selectbox("📁 Choose Subdomain", list(quiz_bank[domain].keys()))

# Initialize only once
if (
    "questions" not in st.session_state
    or st.session_state.get("last_domain") != domain
    or st.session_state.get("last_subdomain") != subdomain
):
    st.session_state.questions = quiz_bank[domain][subdomain].copy()
    random.shuffle(st.session_state.questions)
    st.session_state.answers = [None] * len(st.session_state.questions)
    st.session_state.submitted = False
    st.session_state.score = 0
    st.session_state.score_saved = False
    st.session_state.last_domain = domain
    st.session_state.last_subdomain = subdomain

# Show Questions
for i, q in enumerate(st.session_state.questions):
    st.markdown(f"**Q{i+1}: {q['question']}**")
    st.session_state.answers[i] = st.radio(
        f"Choose an option for Q{i+1}",
        q["options"],
        key=f"q_{i}",
        disabled=st.session_state.submitted or st.session_state.time_up
    )
    st.divider()

# Submit manually
if not st.session_state.submitted and not st.session_state.time_up:
    if st.button("✅ Submit Quiz"):
        st.session_state.submitted = True

# Auto-submit if time's up
if st.session_state.time_up and not st.session_state.submitted:
    st.session_state.submitted = True

# Evaluate
if st.session_state.submitted and not st.session_state.score_saved:
    score = 0
    for i, q in enumerate(st.session_state.questions):
        if st.session_state.answers[i] == q["answer"]:
            score += 1
    st.session_state.score = score
    st.session_state.score_saved = True

    st.success(f"🎉 {name}, you scored {score} out of {len(st.session_state.questions)}!")

    score_data = {
        "Name": name,
        "Domain": domain,
        "Subdomain": subdomain,
        "Score": score,
        "Total": len(st.session_state.questions),
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    new_df = pd.DataFrame([score_data])
    file_path = "score_history.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, new_df], ignore_index=True)
    else:
        df = new_df
    df.to_csv(file_path, index=False)

# Review Answers
if st.session_state.submitted:
    st.subheader("📋 Answer Review:")
    for i, q in enumerate(st.session_state.questions):
        user_ans = st.session_state.answers[i]
        correct_ans = q["answer"]
        if user_ans == correct_ans:
            st.success(f"✅ Q{i+1}: Correct - {correct_ans}")
        else:
            st.error(f"❌ Q{i+1}: Your Answer: {user_ans} | Correct Answer: {correct_ans}")

# Show Score History
st.subheader("📊 Your Score History")
try:
    df = pd.read_csv("score_history.csv")
    user_scores = df[df["Name"] == name].sort_values(by="Date", ascending=False)
    st.dataframe(user_scores.reset_index(drop=True))
except FileNotFoundError:
    st.info("No score history found yet.")

# ⏱️ Timer refresh logic at bottom so rest of app loads before rerun
if not st.session_state.submitted and not st.session_state.time_up:
    time.sleep(1)
    st.rerun()