import traceback
import streamlit as st
from agent import get_response

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Agent",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.title("⚙️ AI Agent Settings")

    st.markdown("### 🤖 Model")
    st.info("Qwen3:8B")

    st.markdown("### 🧠 Memory")
    st.success("Persistent Memory Enabled")

    st.markdown("### 🛠 Available Tools")
    st.success("🔍 DuckDuckGo Search")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "👋 Hi! I'm your AI assistant. Ask me anything."
            }
        ]
        st.rerun()

# -------------------------------
# Main Title
# -------------------------------
st.title("🤖 Personal AI Assistant")
st.caption("Powered by Qwen3 + LangChain + Streamlit")

# -------------------------------
# Initialize Chat History
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hi! I'm your AI assistant. Ask me anything."
        }
    ]

# -------------------------------
# Display Previous Messages
# -------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------
# Chat Input
# -------------------------------
prompt = st.chat_input("Type your message here...")

# -------------------------------
# User Sends a Message
# -------------------------------
if prompt:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("🧠 Thinking..."):
            try:
                reply = get_response(prompt)
            except Exception as e:
                reply = f"```text\n{traceback.format_exc()}\n```"

        st.markdown(reply)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    