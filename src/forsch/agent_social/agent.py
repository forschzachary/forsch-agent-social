"""social agent definition."""

from google.adk import Agent

agent = Agent(
    name="social_agent",
    model="gemini-2.5-flash",
    instruction="You are the social team lead for Forsch.",
)
