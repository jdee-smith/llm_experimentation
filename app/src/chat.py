import duckdb
from langchain_community.llms import Ollama


class Chat:
    initialized = False

    def __init__(self):
        self.model = Ollama(model="llama2")

    def initialize(self):
        self.initialized = True

    def ask(self, query: str):
        if not self.initialized:
            return "Please initialize with a baseline scenario."

        return duckdb.sql("SELECT * FROM baseline")

    def clear(self):
        self.initialized = False
