import os

# Define the folder and file structure with vector databases
structure = {
    "astraX": {
        "llms": ["__init__.py", "factory.py", "openai_llm.py", "huggingface_llm.py", "deepseek_llm.py"],
        "embeddings": ["__init__.py", "factory.py", "openai_embedder.py", "huggingface_embedder.py", "glove_embedder.py", "custom_embedder.py"],
        "chains": ["__init__.py", "simple.py", "sequential.py", "parallel.py"],
        "splitters": ["__init__.py", "text_splitter.py", "html_splitter.py"],
        "databases": ["__init__.py", "chroma_db.py", "faiss_db.py", "pinecone_db.py", "weaviate_db.py"],
        "utils": ["__init__.py", "loader.py", "helpers.py"],
        "templates": ["template.py"],
        "__init__.py": [],
    },
    ".env": [],
}

# Function to create the folder structure
def create_structure(base_path, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                pass  # Create an empty file

# Create the folder structure
base_path = os.getcwd()  # Current working directory
create_structure(base_path, structure)

print("Folder structure with vector databases created successfully!")
