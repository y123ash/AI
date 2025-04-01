# agent_core.py
#from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class BaseAgent:
    def __init__(self, model_name="gpt-3.5-turbo", temperature=0):
        self.llm = OpenAI(model_name=model_name, temperature=temperature)

    def ask(self, prompt: str) -> str:
        response = self.llm(prompt)
        return response
