# test_agents.py
import os
import sys
from agents.workflow_agent import WorkflowAgent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def test_workflow_agent_medical_query():
    workflow_agent = WorkflowAgent()
    response = workflow_agent.delegate_task("medical_query", "What are symptoms of hypertension?")
    assert response is not None
    assert "symptoms" in response.lower()

# test_agents.py
from agents.agentic_manager import AgenticManager

def test_agentic_manager_goals():
    agentic_manager = AgenticManager()
    agentic_manager.add_goal("medical_query", "What is diabetes?")
    responses = agentic_manager.execute_goals()
    
    assert len(responses) == 1
    assert "diabetes" in responses[0].lower()

from services.vector_db import VectorDB

def test_agentic_manager_goals():
    # Explicitly add sample knowledge
    db = VectorDB()
    db.add_document("doc1", "Diabetes is a chronic condition characterized by high blood sugar.")

    agentic_manager = AgenticManager()
    agentic_manager.add_goal("medical_query", "What is diabetes?")
    responses = agentic_manager.execute_goals()

    assert len(responses) == 1
    assert "chronic condition" in responses[0].lower()