import streamlit as st
import re

st.set_page_config(page_title="Passsword Strength Meter", page_icon="🔒")
st.title("🔐Password Strength Meter")
st.markdown("""
Welcome to the ultimate password strength meter!👋 use this simple tool to check the strength of your password and get suggestions on how to make it stronger, we will give you helpful tips to create a **Strong Password** 🔒 """)
password = st.text_input("Enter your password", type = "password")
feedback = []
score = 0   
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters.")
    if re.search(r'/d', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit.")
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character(!@#$%&*).")
    if score == 4:
        feedback.append("✅Your password is strong.🎉")
    elif score == 3:
        feedback.append("🟡Your password is medium strenght.It could be stronger.")
    else:
        feedback.append("🔴Your password is weak.Please make it stronger.")
    
    if feedback:
        st.markdown('## Improvement Suggestions')
    for tip in feedback:
        st.write(tip)
    else:
        st.info('please enter your password to get started')
  
  

# new_env\Scripts\activate
# pip install streamlit
# streamlit run Password.py

# G7$tR!xQp@92zE

# M@xWell!2034*z

# vY#R3@t5Lp!2Qx

# Zebra!2025$Rock

# C@tchM3If_UC4n

