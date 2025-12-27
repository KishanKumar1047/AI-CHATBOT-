# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Choose the model HERE
# model = genai.GenerativeModel("gemini-2.5-flash")# gemini-pro
# chat=model.start_chat(history=[])

# def get_gemini_response(question):
#     response = chat.send_message(question,stream=True )
#     return response


# ## initialize the streamlit app
# st.set_page_config(page_title="Q & A Demo")
# st.header("Gemini LLM Application")

# #initialize user input
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# input=st.text_input("Input:", key="input")
# submit=st.button("Ask the question")

# if submit and input:
#     response=get_gemini_response(input)
#     # add user query and response to chat history
#     st.session_state.chat_history.append(("you", input))
#     st.subheader("Response from Gemini LLM")
#     for chunk in response:
#         st.write(chunk.text)    
#         st.session_state.chat_history.append(("Agent", chunk.text))
        
# st.subheader("Chat History")

# for role,text in st.session_state.chat_history:
#     if role=="you":
#         st.markdown(f"**You:** {text}")
#     else:
#         st.markdown(f"**Agent:** {text}")

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# =========================
# CONFIG
# =========================
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# =========================
# SYSTEM PROMPTS
# =========================
SYSTEM_PROMPTS = {
    "Chatbot": "You are a helpful, friendly conversational AI chatbot.",
    "Coding": "You are a coding assistant. Provide clean, correct code.",
    "DSA": "You are a DSA expert. Return optimized C++ code without comments.",
    "MCQ": "Answer MCQs with only the correct option and a very short explanation.",
    "Debug": "You are a debugging assistant. Identify and fix errors clearly."
}

# =========================
# HELPER: BUILD CONTEXT
# =========================
def build_prompt(messages, system_prompt):
    prompt = system_prompt + "\n\n"
    for msg in messages:
        role = "User" if msg["role"] == "user" else "Assistant"
        prompt += f"{role}: {msg['content']}\n"
    prompt += "Assistant:"
    return prompt

# =========================
# SESSION STATE
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "is_generating" not in st.session_state:
    st.session_state.is_generating = False

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("⚙️ Settings")

    theme = st.radio("Theme", ["Light", "Dark"])
    mode = st.selectbox("Mode", list(SYSTEM_PROMPTS.keys()))
    temperature = st.slider("Creativity", 0.0, 1.0, 0.3)

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.session_state.is_generating = False
        st.rerun()

# =========================
# THEME COLORS
# =========================
if theme == "Dark":
    bg = "#343541"
    user_bg = "#3e3f4b"
    bot_bg = "#444654"
    text = "#ececf1"
    code_bg = "#1f2937"
else:
    bg = "#f7f7f8"
    user_bg = "#e5e7eb"
    bot_bg = "#ffffff"
    text = "#111827"
    code_bg = "#111827"

# =========================
# CSS
# =========================
st.markdown(f"""
<style>
body {{
    background-color: {bg};
}}

.chat-container {{
    max-width: 760px;
    margin: auto;
}}

.user {{
    background: {user_bg};
    color: {text};
    padding: 14px;
    border-radius: 12px;
    margin: 12px 0 12px auto;
    max-width: 85%;
}}

.bot {{
    background: {bot_bg};
    color: {text};
    padding: 14px;
    border-radius: 12px;
    margin: 12px auto 12px 0;
    max-width: 85%;
    border: 1px solid #8884;
}}

.role {{
    font-size: 12px;
    opacity: 0.6;
    margin-bottom: 6px;
}}

pre {{
    background: {code_bg};
    color: #f9fafb;
    padding: 14px;
    border-radius: 10px;
    overflow-x: auto;
}}

code {{
    background: {code_bg};
    color: #f9fafb;
    padding: 4px 6px;
    border-radius: 6px;
}}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown("<h2 style='text-align:center'>🤖 AI Chatbot</h2>", unsafe_allow_html=True)
st.caption("ChatGPT-style chatbot powered by Gemini")

# =========================
# CHAT HISTORY DISPLAY
# =========================
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    cls = "user" if msg["role"] == "user" else "bot"
    name = "You 👤" if msg["role"] == "user" else "Bot 🤖"

    st.markdown(
        f"""
        <div class="{cls}">
            <div class="role">{name}</div>
            {msg["content"]}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# INPUT (GENERATION LOCK FIX)
# =========================
prompt = st.chat_input("Message the chatbot...")

if prompt and not st.session_state.is_generating:
    st.session_state.is_generating = True

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Build context
    final_prompt = build_prompt(
        st.session_state.messages,
        SYSTEM_PROMPTS[mode]
    )

    model = genai.GenerativeModel(
        MODEL_NAME,
        generation_config={"temperature": temperature}
    )

    placeholder = st.empty()
    full_response = ""

    response = model.generate_content(final_prompt, stream=True)

    for chunk in response:
        if chunk.text:
            full_response += chunk.text
            placeholder.markdown(
                f"""
                <div class="bot">
                    <div class="role">Bot 🤖</div>
                    {full_response}▌
                </div>
                """,
                unsafe_allow_html=True
            )

    placeholder.markdown(
        f"""
        <div class="bot">
            <div class="role">Bot 🤖</div>
            {full_response}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Save assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )

    st.session_state.is_generating = False

