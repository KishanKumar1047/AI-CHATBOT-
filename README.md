Here’s a **clean, professional `README.md`** you can directly drop into your project.
It’s written like a **real GitHub project**, clear, concise, and future-proof.

---

# 🤖 AI Chatbot (ChatGPT-Style) — Powered by Gemini

A **ChatGPT-style conversational AI chatbot** built with **Streamlit** and **Google Gemini**, featuring a modern UI, real-time streaming responses, multiple intelligent modes, and stable chat history handling.

This is **not a demo** — it’s a production-ready chatbot foundation.

---

## ✨ Features

### 💬 Chat Experience

* ChatGPT-style conversation UI
* Real-time streaming responses
* Stable two-way chat (no duplicate or one-way replies)
* Persistent in-session chat history
* Clean message bubbles with avatars

### 🎨 UI / UX

* Light & Dark mode
* ChatGPT-inspired layout
* Styled code blocks
* Smooth interaction with Streamlit reruns handled correctly

### 🧠 Intelligence Modes

Switch chatbot behavior instantly:

* **Chatbot** – friendly conversational assistant
* **Coding** – clean, correct code generation
* **DSA** – optimized C++ solutions (no comments)
* **MCQ** – direct answer with short explanation
* **Debug** – error analysis and fixes

### ⚙️ Controls

* Creativity (temperature) slider
* Theme toggle
* Mode selector
* Clear chat button
* Safe generation lock (prevents bot self-reply)

---

## 🧩 Tech Stack

* **Frontend / UI**: Streamlit
* **LLM**: Google Gemini (`gemini-2.5-flash`)
* **Language**: Python
* **Environment Management**: `python-dotenv`

---

## 📁 Project Structure

```text
ai-chatbot/
│
├── qachat.py              # Main Streamlit application
├── .env                # Environment variables (API key)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kishankumar1047/ai-chatbot.git
cd ai-chatbot
```

---

### 2️⃣ Create & Activate Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

> 🔐 Never commit your `.env` file to GitHub.

---

### 5️⃣ Run the Application

```bash
streamlit run qachat.py
```

The chatbot will be available at:

```
http://localhost:8501
```

---

## 🧠 How Chat History Works (Important)

* Chat history is stored in `st.session_state.messages`
* Only **one source of truth** is used (prevents desync)
* A **generation lock** prevents duplicate responses during Streamlit reruns
* Sidebar interactions do **not** trigger unintended bot replies

This ensures **true two-way conversation**, just like ChatGPT.

---

## 🛡️ Known Safeguards

* ✅ No bot replying to itself
* ✅ Sidebar rerun protection
* ✅ Stable memory handling
* ✅ Clean prompt construction per turn

---

## 🔮 Future Enhancements

* Auto-scroll to latest message
* Copy button for messages & code blocks
* Persistent chat storage (SQLite / MongoDB)
* File & image input (Gemini Vision)
* Chrome extension UI
* User authentication & saved chats
* Deployment on Streamlit Cloud / AWS

---
## 🤝 Contributing

Contributions are welcome!

* Fork the repository
* Create a feature branch
* Submit a pull request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Acknowledgements

* **Google Gemini** for the LLM
* **Streamlit** for rapid UI development
* Inspired by **ChatGPT’s conversational design**

---

## 🙌 Author

Built with ❤️ by **Kishan**

---

If you want, I can also generate:

* `requirements.txt`
* `.gitignore`
* deployment instructions
* GitHub badges
* demo GIF script

Just say the word 🚀
