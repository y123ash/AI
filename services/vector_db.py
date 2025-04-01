# vector_db.py
import chromadb
from chromadb.config import Settings
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class VectorDB:
    def __init__(self, db_path='medical_kb'):
        self.client = chromadb.PersistentClient(path=db_path, settings=Settings(allow_reset=True))
        self.collection = self.client.get_or_create_collection("medical_documents")

    def add_document(self, doc_id: str, content: str):
        self.collection.add(ids=[doc_id], documents=[content])

    def query(self, query_text: str, n_results=1):
        results = self.collection.query(query_texts=[query_text], n_results=n_results)
        return results['documents'][0]