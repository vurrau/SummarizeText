import uvicorn
from fastapi import FastAPI
from langchain_huggingface.llms import HuggingFacePipeline

app = FastAPI()

# Create a HuggingFacePipeline for the summarization model
hf_pipeline = HuggingFacePipeline.from_model_id(
    model_id="facebook/bart-large-cnn",
    task="summarization",
    pipeline_kwargs={"max_new_tokens": 150},
)


@app.post("/summarize")
async def summarize(request: str):
    summary = hf_pipeline(request)
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)