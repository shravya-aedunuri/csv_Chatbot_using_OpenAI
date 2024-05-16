# Langchain_powered_chatbot
Leveraging Langchain Powered Question-Answering System using OpenAI


**Project Description**

This project integrates Langchain with GPT-3.5 Turbo for medical query resolution, comparing its performance with prompt-based models and analyzing Cancer Genome Atlas reports using NLP, evaluating With-Indexing and Without-Indexing models.

**Objectives**

- Propose methodologies to implement the RAG model in medical contexts, providing practical insights into leveraging generative AI for healthcare applications.

- Implement indexing with Langchain, GPT-3.5 Turbo, and Chroma Vector database for tailored AI responses aligned with dataset content and specific queries.

**Methodology**

System Architecture:


![image](https://github.com/shravya-aedunuri/Langchain_powered_chatbot/assets/66987710/50f42e56-5451-4f3d-af29-81c92978f617)


**Without Indexing**

In without indexing response is solely dependent on LLM. I'm using GPT 3.5 turbo as LLM.


**With Indexing:**
- Data Collection: Gathering data needed for the research.
- Data Loading:Loading the data using csv Loader.
- Chunking: Breaking down the text into smaller data called chunks.
- Embedding: Converting the chunks into numerical vectors using Sentence Transformer Embeddings.
- Vector Database: Storing embeddings for efficient search using Chroma Vector databases.
- Similarity Search: Using vector database to find the top most similar data to a query.
- Integration and Answer Generation: Search for contextually relevant information and integrate with prompted questions and generate responses using GPT-3.5 Turbo integrated with Langchain.
  
  
**Metrics to evaluate RAG:**

- Cosine similarity is a mathematical measure used to determine the degree of similarity particularly in the context of text embedding similarity tasks.
- Cosine similarity ranges from -1 to 1.Cosine distance is a metric used to measure the similarity between two vectors in a high-dimensional space. This score ranges from 0 to 2.
- Cosine distance score is inversely proportional to similarity. i.e. lower cosine distance score means higher similarity.
- Here, Cosine similarity distance score is computed between the vectors of prompts and the vectors of with index responses.




![image](https://github.com/shravya-aedunuri/Langchain_powered_chatbot/assets/66987710/a37c3371-7e76-4a79-b9ee-924df9115e68)


![image](https://github.com/shravya-aedunuri/Langchain_powered_chatbot/assets/66987710/44a3a323-66db-40ce-8bf0-691eff6f3bb3)

We can see in Figure 1, when some 5 general prompts were asked and which are not very specific to dataset, It is observed that the cosine distance is around 0.25. From Figure 2 we can observe when the prompts are more specific to dataset. It can be seen that the cosine distance got lowered, it is around 0.08.


**Tools Used**

Programming Language: Python.

Software Requirements: Technology: Python 3.6,IDE: Google Colaboratory.

Hardware Requirements: Processor: Any Update Processor RAM with min 4GB and Hard Disk with min 100GB.

Attached
 
The repository contains GoogleColab Notebook

**Conclusion**

The comparison between "with indexing" and "without indexing" methodologies underscores the benefits of structured data retrieval strategies. Integration of LangChain, GPT-3.5, and a vector database in the "with indexing" approach provides a systematic framework for tailored responses, particularly beneficial in healthcare analyses like cancer patient data. This structured methodology enhances precision, facilitates targeted insights, and improves decision-making processes, showcasing promise for practical AI applications. 
LangChain integrates retrieval techniques with text generation algorithms to deliver precise and contextually appropriate responses to user inquiries.
