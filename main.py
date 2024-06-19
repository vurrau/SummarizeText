import uvicorn
from fastapi import FastAPI
from langchain_huggingface.llms import HuggingFacePipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

app = FastAPI()

model_id = "facebook/bart-large-cnn"  # Specify the model and the task
task = "summarization"

tokenizer = AutoTokenizer.from_pretrained(model_id)  # Load the tokenizer and model
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline(task, model=model, tokenizer=tokenizer)  # Create pipeline
hf_pipeline = HuggingFacePipeline(pipeline=pipe)  # Create an instance of HuggingFacePipeline specifying a pipeline


@app.post("/summarize")
async def summarize(request: str):
    summary = hf_pipeline(request)
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

