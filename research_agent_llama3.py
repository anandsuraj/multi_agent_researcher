# Import the required libraries
import streamlit as st
from agno.agent import Agent  # Main agent class for creating AI agents
from agno.tools.hackernews import HackerNews  # Tool to interact with Hacker News API
from agno.models.ollama import Ollama  # Language model interface for Llama-3

# Set up the Streamlit web interface
st.title("Multi-Agent AI Research Assistant using Llama-3 🔍🤖")
st.caption("Explore top tech stories and influential users from Hacker News using AI-powered research agents.")

# Initialize the first specialized agent for analyzing stories
story_researcher = Agent(
    name="Story Insights Analyst",
    role="Fetches and analyzes top stories from Hacker News.",
    tools=[HackerNews()],  # Equip agent with Hacker News API access
    model=Ollama(id="llama3.2", max_tokens=1024)  # Configure Llama-3 model with token limit
)

# Initialize the second specialized agent for analyzing users
user_researcher = Agent(
    name="User Insights Explorer",
    role="Investigates Hacker News user profiles and activity.",
    tools=[HackerNews()],  # Equip agent with Hacker News API access
    model=Ollama(id="llama3.2", max_tokens=1024)  # Configure Llama-3 model with token limit
)

# Create a master agent that coordinates both specialized agents
hn_assistant = Agent(
    name="Hacker News Research Collective",
    team=[story_researcher, user_researcher],  # Combine both agents into a team
    model=Ollama(id="llama3.2", max_tokens=1024)  # Configure main agent's model
)

# Create input field in Streamlit UI for user queries
query = st.text_input("What would you like to investigate today?")

# Process the query when user inputs something
if query:
    # Execute the query using the master agent and display results
    response = hn_assistant.run(query, stream=False)  # stream=False means wait for complete response
    st.write(response.content)  # Display the response in the Streamlit interface