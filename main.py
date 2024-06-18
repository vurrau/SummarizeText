from fastapi import FastAPI
import uvicorn
from transformers import pipeline

app = FastAPI()


@app.post("/summarize")
async def summarize(request: str):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # AI by Hugging Face
    summary = summarizer(request, max_length=130, min_length=30, do_sample=False)  # cfg AI
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)