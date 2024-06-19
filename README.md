# SummarizeText API

This project provides a FastAPI endpoint for summarizing text using the AI by Hugging Face library.

## Setup

### 1. Create a virtual environment

To create and activate a virtual environment, follow these steps:

```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
### 2. Install dependencies:
```
pip install langchain langchain-huggingface transformers huggingface_hub
```
### 3. Run the application:
```
uvicorn main:app --reload
```
### 4. Test the endpoint:
- Send a POST request to ```http://127.0.0.1:8000/summarize``` with a JSON body containing the text to be summarized.