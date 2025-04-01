# agentic_manager.py
from agents.workflow_agent import WorkflowAgent
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class AgenticManager:
    def __init__(self):
        self.workflow_agent = WorkflowAgent()
        self.goals = []

    def add_goal(self, goal_type: str, content: str):
        self.goals.append((goal_type, content))

    def execute_goals(self):
        results = []
        for goal_type, content in self.goals:
            if goal_type == "medical_query":
                result = self.workflow_agent.delegate_task(goal_type, content)
                results.append(result)
            else:
                results.append("Goal type not supported.")
        return results