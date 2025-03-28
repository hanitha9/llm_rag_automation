import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from automation_functions import FUNCTION_METADATA

class RAGEngine:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)
        self.function_names = list(FUNCTION_METADATA.keys())
        self._build_index()

    def _build_index(self):
        if not FUNCTION_METADATA:
            print("No functions in metadata to build index")
            return
        descriptions = [FUNCTION_METADATA[func]["description"] for func in self.function_names]
        embeddings = self.model.encode(descriptions)
        self.index = faiss.IndexFlatL2(384)  # Reinitialize index
        self.index.add(np.array(embeddings).astype('float32'))
        self.function_names = list(FUNCTION_METADATA.keys())
        print(f"Index built with {len(self.function_names)} functions")

    def retrieve_function(self, query):
        if not self.function_names:
            print("No functions available to retrieve")
            return None
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding).astype('float32'), 1)
        if indices.size == 0 or indices[0][0] >= len(self.function_names):
            print(f"Index error: {indices} out of range for {len(self.function_names)} functions")
            return self.function_names[0] if self.function_names else None
        return self.function_names[indices[0][0]]

    def maintain_context(self, chat_history, current_query):
        if not chat_history:
            return self.retrieve_function(current_query)
        
        query_lower = current_query.lower()
        print(f"Checking query: {query_lower}")
        print(f"Available functions: {self.function_names}")
        
        for func in self.function_names:
            func_name = func.replace("_", " ")
            print(f"Testing match: '{func_name}' in '{query_lower}'")
            if func_name in query_lower or func in query_lower:
                print(f"Matched function name: {func}")
                return func
        
        function_name = self.retrieve_function(current_query)
        print(f"Vector search result: {function_name}")
        
        if "it" in query_lower or "again" in query_lower:
            context = " ".join([entry["prompt"] for entry in chat_history[-1:]])
            combined_query = f"{current_query} (context: {context})"
            print(f"Using context: {combined_query}")
            context_lower = combined_query.lower()
            for func in self.function_names:
                func_name = func.replace("_", " ")
                print(f"Testing context match: '{func_name}' in '{context_lower}'")
                if func_name in context_lower or func in context_lower:
                    print(f"Matched function from context: {func}")
                    return func
            return self.retrieve_function(combined_query)
        
        return function_name
