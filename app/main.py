import os
import subprocess
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings.openai import OpenAIEmbeddings

DATA_DIR = './data'

# os.environ["OPENAI_API_KEY"] = "YOUR_KEY_HERE"

################################################################################
# Load the data
################################################################################

# Clone the Kubecost "Docs" repo
repository_url = 'https://github.com/kubecost/docs.git'
target_directory = DATA_DIR + '/docs'
if os.path.exists(target_directory):
    print(f"Directory '{target_directory}' already exists. Performing git pull instead.")
    subprocess.run(['cd', target_directory], shell=True)
    subprocess.run(['git', 'pull'], cwd=target_directory)
else:
    subprocess.run(['git', 'clone', '-q', repository_url, target_directory])

# Recursively load all ".md" and ".txt" files from DATA_DIR
loaders = []
for root, dirs, files in os.walk(DATA_DIR):
    for file in files:
        file_path = os.path.join(root, file)
        if ".md" in file_path or ".txt" in file_path:
            print(file_path)
            loaders.append(TextLoader(file_path, encoding='utf8'))

################################################################################
# Create the vectorstore
################################################################################

index = VectorstoreIndexCreator().from_loaders(loaders)

################################################################################
# Query the index
################################################################################

query = "What should my cloud-integration.json secret look like?"
query = "I've just installed my cloud billing integration, but I don't see any reconciled prices. Why?"
index.query_with_sources(query)
