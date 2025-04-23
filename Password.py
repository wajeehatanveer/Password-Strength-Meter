import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
st.title("🔐Password Strength Meter")

st.markdown("""
Welcome to the ultimate password strength meter!👋 Use this simple tool to check the strength of your password and get suggestions on how to make it stronger. We will give you helpful tips to create a **Strong Password** 🔒
""")

password = st.text_input("Enter your password", type="password")
feedback = []
score = 0

if password:
    # 1. Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # 2. Upper and lower case check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case characters.")

    # 3. Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # 4. Special character check
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%&*).")

    # Strength judgment
    if score == 4:
        feedback.append("✅ Your password is strong. 🎉")
    elif score == 3:
        feedback.append("🟡 Your password is medium strength. It could be stronger.")
    else:
        feedback.append("🔴 Your password is weak. Please make it stronger.")

    # Feedback show karna sirf agar kuch ho
    if feedback:
        st.markdown('## Improvement Suggestions')
        for tip in feedback:
            st.write(tip)

else:
    # User ne kuch type nahi kiya
    st.info('Please enter your password to get started.')
