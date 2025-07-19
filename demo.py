import math
import ollama

#loading dataset and initializing Ollama models
DATA_FILE = 'cat-facts.txt'
EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'
dataset = []
with open(r'C:\Users\sharm\Desktop\ANLPHW1\cat-facts.txt', encoding='utf-8') as file:
    dataset = [line.strip() for line in file if line.strip()]

VECTOR_DB = []
#chunking the dataset and adding to vector database
# In this case, each line in the dataset is treated as a chunk.
def add_chunk_to_database(chunk):
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
    VECTOR_DB.append((chunk, embedding))

for chunk in dataset:
    add_chunk_to_database(chunk)
# Function to calculate cosine similarity between two vectors
# This is used to find the most relevant chunks in the vector database.
def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b)

# Function to retrieve the most relevant chunks from the vector database
# based on the cosine similarity of their embeddings with the query embedding.
def retrieve(query, top_n=3):
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]
    similarities = [(chunk, cosine_similarity(query_embedding, emb)) for chunk, emb in VECTOR_DB]
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_n]

# Function to generate a response using the Ollama chat model
# It retrieves relevant knowledge from the vector database and formats it
# into a prompt for the language model.
# The response is streamed back to the user.
def generate_response(input_query):
    retrieved_knowledge = retrieve(input_query)
    print('Retrieved knowledge:')
    for chunk, similarity in retrieved_knowledge:
        print(f' - (similarity: {similarity:.2f}) {chunk}')
    instruction_prompt = f"""You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
{chr(10).join([f' - {chunk}' for chunk, _ in retrieved_knowledge])}
"""
    stream = ollama.chat(
        model=LANGUAGE_MODEL,
        messages=[
            {'role': 'system', 'content': instruction_prompt},
            {'role': 'user', 'content': input_query},
        ],
        stream=True,
    )

    print('\n Chatbot response:')
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
# This is the main loop that allows the user to interact with the chatbot.
# The user can ask questions, and the chatbot will respond based on the knowledge retrieved from the vector database.
if __name__ == '__main__':
    while True:
        try:
            input_query = input('\n what is your question? (type "exit" to quit): ')
            if input_query.strip().lower() == 'exit':
                break
            generate_response(input_query)
        except KeyboardInterrupt:
            break