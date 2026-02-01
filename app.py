import streamlit as st
from transformers import pipeline

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="GenAI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Generative AI Chatbot")
st.write("A simple chatbot powered by Generative AI")

# ---------------- Load Model ----------------
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# ---------------- Chat History ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- User Input ----------------
user_input = st.text_input(
    "You:",
    placeholder="Ask me anything..."
)

if st.button("Send"):
    if user_input.strip() != "":
        with st.spinner("Thinking..."):
            response = generator(
                user_input,
                max_length=120,
                temperature=0.7
            )

            bot_reply = response[0]["generated_text"]

            st.session_state.messages.append(("You", user_input))
            st.session_state.messages.append(("Bot", bot_reply))

# ---------------- Display Messages ----------------
for role, text in st.session_state.messages:
    if role == "You":
        st.markdown(f"**🧑 You:** {text}")
    else:
        st.markdown(f"**🤖 Bot:** {text}")

