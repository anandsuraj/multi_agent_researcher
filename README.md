# 🧠 Multi-Agent AI Researcher

A smart, interactive research tool that helps you explore HackerNews like never before — using the power of **AI agents powered by GPT-4o**.

## 🔍 What Is This?

This is a **Streamlit-powered app** that uses multiple AI assistants working together to help you:

- Discover top stories on [HackerNews](https://news.ycombinator.com/)
- Research active users
- Generate insightful blog posts, reports, or social media updates based on what you're curious about

Think of it as a team of expert researchers in your pocket — all running on AI.

---

## 🚀 How to Get Started

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/anandsuraj/multi_agent_researcher.git
cd multi_agent_researcher
```

### 2. Install Dependencies

Make sure you have Python installed (preferably 3.9+), then install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Get an OpenAI API Key

You'll need access to OpenAI's GPT-4 model. Follow these steps:

- Sign up at [OpenAI Platform](https://platform.openai.com/)
- Create an API key from your dashboard
- Keep this key handy — you’ll enter it when you start the app

> 💡 Pro tip: Never share or commit your API key publicly.

### 4. Launch the App

Run the app with:

```bash
streamlit run research_agent.py
```

Or if you're using a virtual environment:

```bash
./venv/bin/python -m streamlit run research_agent.py
```

Then open the link shown in your browser.

---

## 🤖 How It Works

When you launch the app:

1. You’ll be asked to **enter your OpenAI API key**
2. Behind the scenes, three AI agents are created:
   - **Story Researcher**: Specializes in digging into HackerNews stories
   - **User Researcher**: Focuses on user profiles, activity, and article summaries
   - **HN Assistant**: Your main assistant who coordinates between the two researchers

3. Type in your research question or topic (e.g., *"What are the most popular AI stories this week?"* or *"Tell me about user 'pg' on HackerNews."*)

4. The HN Assistant takes over:
   - Decides which agent should do what
   - Fetches data from HackerNews
   - Uses GPT-4o to generate a well-written summary or content piece

5. You get a **clear, well-structured output**, ready to use for blogging, reporting, or sharing!

---

## 📌 Example Use Cases

Here are some things you can ask:

- _"Summarize the top 5 stories from HackerNews today."_
- _"Who is the user 'dhh' on HackerNews?"_
- _"Write a Twitter/X thread about the latest trends in AI from HackerNews."_
- _"Generate a blog post summarizing the best productivity advice from recent HackerNews threads."_

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io): For the web interface
- [OpenAI GPT-4o](https://openai.com/index/gpt-4o/): To power the AI agents
- [LangChain](https://www.langchain.com): For managing tools and agent workflows
- [Python](https://python.org): Core programming language

---

## ✅ Future Enhancements (Ideas)

- Support for more platforms beyond HackerNews
- Export generated content to PDF or Markdown
- Save and reuse previous research queries
- Add support for other LLM providers (like Anthropic, Gemini, etc.)

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the app, fix bugs, or add features, feel free to open a PR or issue on GitHub.

---

## 📬 Feedback & Questions?

If you have any questions, suggestions, or want to collaborate, reach out to the repo owner or open an issue on GitHub.

---

Enjoy researching smarter with AI! 🚀  
Let the agents do the heavy lifting while you focus on asking great questions.

--- 
