Simple Retrieval Augmented Generation chatbot with ollama.


What my code does?
1- Loads a list of short facts from a text file cat-facts.txt.
2- Converts each fact into a vector using an embedding model.
3- Saves these vectors in a list for later use.
4- user ask a question to the model
5- question gets converted into a vector.
6- The code compares this vector to all stored ones using cosine similarity.
7- It selects the most relevant facts based on similarity.
8- These facts are used to create a prompt.
9- language model then generates an answer using only that information.

How to run the code:

1-Python 3.8 or higher
2- download and install Ollama from https://ollama.com
3-open ollama settings
4-check the models folder --copy the path--and turn on the connection button.
5- open your cmd, go to your models path and paste command in terminal ollama pull hf.co/CompendiumLabs/bge-base-en-v1.5-gguf ollama pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF.
6-Install the Python package: pip install ollama
7-Run the script.
8- type your question in terminal
9- type exit



Limitations:
1- Retrieval depends on word similarities only and not deeper sementic meanings.
2- The model won’t answer well if relevant information is missing from the dataset.
3- If a question doesn't match how the facts are written, retrieval might fail.
4- dataset is very small and may have biases.
5- Responses are limited to trained dataset wont generate answers to the incidents happend recently.

Improvements:
1- A larger dataset can improve the retrieval results.
2- We can use more advance language models to generate more accurate answers.
3- We can also use knowledge graphs retrieval to introduce factuality.
4- Also we can use multi step reasoning for more accurate answers.

Task 8:

1- top_n=1
it might avoid distraction but while retriving it may miss some important context.

2- top_n=8
braod context many facts, Helpful for vague or open-ended queries.

3- top_n=4
it kind of act as a balance, great for slightlycomplex task.

different promtpts tried:
1- what is the name of the president.
Ans- there is no mention of the president in the given context.
2- where is germany?
Answer:Germany is located in Central Europe, bordered by Denmark to the north, Poland and the Czech Republic to the east, Austria and Switzerland to the south, France and Luxembourg to the southwest, Belgium and the Netherlands to the southeast.


