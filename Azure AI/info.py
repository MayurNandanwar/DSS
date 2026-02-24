Prompt Flow: it is development tool designed to streamline the entire development cycle of AI applications powered by LLMs. 
prompt flow provides comprehensive solution that simplifies the process of 
prototyping, experimenting, iterating and deploying your AI applications.
The flow is exposed as API which can be consumed in your AI Applications.


# compute power is of two way: either you host vertual machine to provide compute power or your flow can run on serverless api bases which is much better way
# to go through. When you designate the VM solely dedicated for supply compute power to run this prompt flow. you will be charged hourly bases which means you will also be charged for the time 
when the promptflow is being idle. But when you go through the way of consuming the prompt flow or deploying the prompt flow via serverless api architecture which means you will be chnaged only when 
prompt flow is executed. you wont be charged when promptflow is left idle. 


With Prompt Flow in Azure AI studio you can:

1) orchestrate executable with LLM, prompts, and python tools through a visualized graph
2) debug share and iteerate your flows with ease through team collaboration.
3) create prompt variants and compare their performance

# promptflow will be used to build small, packaged, complex ai applications.

# steps :
azure ai studio
input:
    define variable :
define prompt flow 
cleaning python operation if required
output:
    result entity format



# example of prompt flow 
# recommand investment advice like any well known person like warren Buffett.

# Step 1: Set Up Azure Resources

    # Azure OpenAI Resource
    # Deploy GPT-4o (or GPT-4 Turbo) in your Azure subscription.
    # Get the endpoint + API key.

# Azure Bing Search Resource
    # In Azure Portal → Create a resource → search Bing Search v7 / Grounding with Bing Search.
    # Get API endpoint + key.

# Prompt Flow in Azure AI Studio
    # Create a Prompt Flow project.
    '''You are Warren Buffett. Provide investment advice in his style, 
        using Bing Search results for real-time context. Cite sources clearly.
        '''

    # Define nodes:
        # User Input
        # Bing Search Tool Node (fetches real-time market data)
        # LLM Node (GPT) → System prompt:


from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

# Load API keys from environment variables
BING_API_KEY = os.getenv("BING_API_KEY")
BING_ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"

PROMPT_FLOW_ENDPOINT = os.getenv("PROMPT_FLOW_ENDPOINT")
PROMPT_FLOW_KEY = os.getenv("PROMPT_FLOW_KEY")

# ---- 1. Bing Search ----
def bing_search(query: str):
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    params = {"q": query, "count": 5}
    response = requests.get(BING_ENDPOINT, headers=headers, params=params)
    return response.json()

# ---- 2. Call Prompt Flow ----
def call_promptflow(user_query, bing_results):
    headers = {
        "Authorization": f"Bearer {PROMPT_FLOW_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": {
            "user_query": user_query,
            "bing_data": bing_results
        }
    }
    response = requests.post(PROMPT_FLOW_ENDPOINT, headers=headers, json=payload)
    return response.json()

# ---- 3. API Endpoint ----
@app.post("/ask")
async def ask_investment(request: Request):
    data = await request.json()
    user_query = data.get("question")

    # Step 1: Get Bing results
    bing_results = bing_search(user_query)

    # Step 2: Call Prompt Flow
    answer = call_promptflow(user_query, bing_results)

    return {"answer": answer}


# RAG : Retriver augmented Generation:
it helps to answer the query of user whose information might  not be in existing database.\



##! How Prompt flow works 
# Deploy embedding model + GPT model in Azure OpenAI.

# Upload documents into Azure Blob Storage.

# Create Azure AI Search index → connect to Blob → generate embeddings → store vectors.

# In Azure AI Studio, connect services: OpenAI, AI Search, Blob.

# Create a Prompt Flow (Standard Flow).

# Add Input node (user query).

# Add Index Lookup node (retrieves similar docs from AI Search).

# Combine query + retrieved docs = augmented context.

# Pass to GPT model node → generate answer.

# Deploy Prompt Flow as real-time endpoint and connect to your app.

