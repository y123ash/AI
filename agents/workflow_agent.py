# workflow_agent.py
from agents.medical_agent import MedicalAgent
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class WorkflowAgent:
    def __init__(self):
        self.medical_agent = MedicalAgent()

    def delegate_task(self, task_type: str, content: str) -> str:
        if task_type == "medical_query":
            return self.medical_agent.handle_medical_query(content)
        else:
            return "Task type not supported yet."