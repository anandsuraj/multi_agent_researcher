import os
import streamlit as st
from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools
from agno.models.openai import OpenAIChat

# --- Page Configuration ---
st.set_page_config(page_title="Multi-Agent AI Researcher", page_icon="🤖", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        /* Background - More contrast gradient */
        .stApp {
            background: linear-gradient(135deg, #61abab 0%, #e8f0e2 80%);
            font-family: 'Segoe UI', sans-serif;
        }

        /* Title - Darker blue for better visibility */
        .main-title {
            color: #1e4b8c;
            font-size: 42px;
            font-weight: 800;
            text-align: center;
            margin-bottom: 5px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
        }

        /* Subtitle - Higher contrast gray */
        .subtitle {
            color: #4a5568;
            font-size: 18px;
            text-align: center;
            margin-bottom: 30px;
            font-weight: 500;
        }

        /* Divider line - Made visible */
        hr {
            border: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #cbd5e0, transparent);
            margin: 25px 0;
        }

        /* API Key Section - Card-style with border */
        .stMarkdown div[data-testid="stMarkdownContainer"] > div:nth-child(2) {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
            color: #2d3748;
            font-weight: 600;
        }

        /* Input Prompt - More prominent */
        .stTextInput > div > div > input {
            background-color: #ffffff;
            border-radius: 12px;
            border: 2px solid #4299e1;
            padding: 12px;
            font-size: 16px;
            color: #1a202c;
            box-shadow: 0 2px 4px rgba(66, 153, 225, 0.15);
        }

        /* Placeholder - More visible */
        .stTextInput > div > div > input::placeholder {
            color: #718096;
            opacity: 0.8;
        }

        /* Example Text - Standout color */
        .stMarkdown div[data-testid="stMarkdownContainer"] > div:nth-child(4) {
            color: #4a5568;
            font-style: italic;
            text-align: center;
            margin-top: 8px;
        }

        /* Footer - Better contrast */
        .footer {
            text-align: center;
            font-size: 13px;
            color: #718096;
            margin-top: 40px;
            padding-top: 15px;
            border-top: 1px solid #e2e8f0;
        }
        
        /* Make the ✔ more visible */
        .footer span {
            color: #38a169;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-title">Multi-Agent AI Research Assistant 🤖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Explore trending stories & contributors on Hacker News with AI agents</div>', unsafe_allow_html=True)

# --- API Key Input ---
openai_api_key = st.text_input("🔑 OpenAI API Key", type="password", placeholder="Paste your OpenAI key here")

# --- Query Input and Agent Execution ---
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key

    # Agents
    story_researcher = Agent(
        name="📰 Story Insights Analyst",
        role="Fetches and analyzes trending stories from Hacker News.",
        tools=[HackerNewsTools()],
    )

    user_researcher = Agent(
        name="👤 User Profile Investigator",
        role="Retrieves and examines Hacker News user profiles and activity.",
        tools=[HackerNewsTools()],
    )

    hn_assistant = Agent(
        name="🧠 Hacker News Intelligence Unit",
        team=[story_researcher, user_researcher],
        model=OpenAIChat(
            id="gpt-4o",
            max_tokens=1024,
            temperature=0.5,
            api_key=openai_api_key
        )
    )

    # --- Query Input ---
    query = st.text_input("🔍 What would you like to research?", placeholder="e.g., Recent AI breakthroughs or Top contributors in LLMs")

    if query:
        with st.spinner("⏳ Gathering insights..."):
            response = hn_assistant.run(query, stream=False)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown("### 📊 Insight Summary")
        st.write(response.content)
        st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown('<div class="footer">Crafted with ❤️ using Streamlit & Agno Agents</div>', unsafe_allow_html=True)
