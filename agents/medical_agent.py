# medical_agent.py
from agents.agent_core import BaseAgent
from services.vector_db import VectorDB
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class MedicalAgent(BaseAgent):
    def handle_medical_query(self, query: str) -> str:
        prompt = f"You are an intelligent medical assistant at Turacoz. Clearly answer:\n{query}"
        return self.ask(prompt)
    def handle_medical_query(self, query: str) -> str:
        relevant_info = self.db.query(query, n_results=1)[0]
        prompt = f"You are an intelligent medical assistant at Turacoz. Clearly answer the question based on the following information:\n{relevant_info}\n\nQuestion: {query}"
        return self.ask(prompt)