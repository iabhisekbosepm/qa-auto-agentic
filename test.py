import os
import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Ensure the Result directory exists
os.makedirs('Result', exist_ok=True)

# Define sensitive data
# The LLM will only see placeholder names (x_Email, x_Password), never the actual values
sensitive_data = {
    'https://checkout.xyz.ai/': {
        'x_Email': 'asdsad@sdf.com',
        'x_Password': 'zKs4%8',
    },
}

# Define your complete custom prompt
override_system_message = """
You are an AI agent that helps users with web browsing tasks.

You are an AI agent that helps users with web browsing tasks.
You are a helpful assistant that can help with tasks such as:
- Searching the web
- Navigating websites
- Finding information
- Answering questions
- And more!

"""

llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

extend_planner_system_message = """
PRIORITIZE gathering information before taking any action.
Always suggest exploring multiple options before making a decision.
"""

planner_llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

# Read the task from to-do.md and prepend smart instructions
with open('to-do.md', 'r') as f:
    gherkin_content = f.read()

meta_instruction = """
You are an advanced QA automation agent.
Your job is to execute and validate ALL scenarios described in the following Gherkin feature file, including scenario outlines with examples.
For each scenario:
- Attempt to perform all steps as described.
- For scenario outlines, iterate through all example rows.
- After each scenario, record whether it passed or failed, and provide a short summary.
- If a step cannot be performed, explain why and mark the scenario as failed.

Here is the feature file:
"""

needtodo = meta_instruction + "\n" + gherkin_content

# Define the agent
async def main():
    agent = Agent(
        task=needtodo,
        llm=llm,
        planner_llm=planner_llm,
        sensitive_data=sensitive_data,
        extend_planner_system_message=extend_planner_system_message,
        save_conversation_path="Result/conversation",  # Save chat logs in Result folder
        override_system_message=override_system_message,
    )
    await agent.run()

asyncio.run(main())