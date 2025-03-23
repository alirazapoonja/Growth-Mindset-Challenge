import streamlit as st # type: ignore

# Custom CSS for styling and animations
def local_css(file_name):  # Use a variable name like `file_name`
    with open(file_name) as f:  # Open the CSS file
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load custom CSS
local_css("style.css")  # Pass the file name as a string

# App Title
st.title("🚀 Growth Mindset Challenge")

# Introduction Section
st.markdown("""
<div class="intro-card">
    <h2>Welcome to the Growth Mindset Challenge!</h2>
    <p>Complete daily tasks to develop a growth mindset and unlock your potential.</p>
</div>
""", unsafe_allow_html=True)

# Daily Challenge Section
st.markdown("""
<div class="challenge-card">
    <h2>GIAIC Python AI Project</h2>
    <p>GIAIC Python AI Project Submission Form</p>
</div>
""", unsafe_allow_html=True)

# Dropdown Menu for Pre-Written Responses
options = [
    "Project One: Growth Mindset Challenge: ",
    "Project Two:  Unit Convertor:",
    "Project Three: Password Strength Meter ",
    "Project Four: Personal Library Manager",
    "Project Five: Building a Todo List Manager",
    "Project Six: Building a Money Making Machine",
    "Project Seven: Building a Time Zone App",
    "Project Eight: Building a Mood Tracker App ",
    "Project Night: Building a Quiz App ",
    "Project Ten: Building a Simple Calculator App",
    "Project Eleven: Building a Random Joke Generator App",
    "Project Twelve: Building a Simple Chatbot App",
    "Project Thirteen: Building a LLM Powered QA Chatbot",
    "Project Fourteen: Building a Stateful Chatbot with Authentication ",
    "Project Fifteen: Building a Simple Agent App ",

]

selected_option = st.selectbox("Choose a response:", options)

# Submit Button
if st.button("Submit"):
    st.markdown(f"""
    <div class="success-message">
        <p>✨ Thank you for completing today's Project!</p>
        <p>Your response: <strong>{selected_option}</strong></p>
    </div>
    """, unsafe_allow_html=True)

# Progress Tracker
st.markdown("""
<div class="progress-card">
    <h2>Your Progress</h2>
    <p>Track how many Projects you've completed so far.</p>
</div>
""", unsafe_allow_html=True)

progress = st.slider("How many Projects have you completed?", 0, 30)
st.write(f"You've completed 👍 {progress} Projects so far. Keep going!")

# Footer
st.markdown("""
<div class="footer">
    <p>Made By 👨‍🎓 Ali Raza</p>
</div>
""", unsafe_allow_html=True)