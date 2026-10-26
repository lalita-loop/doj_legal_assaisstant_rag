from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def index():
    return {"message": "Hello World"}
@app.get("/ask")
def ask_doj(question: str):
    return {"answer": f"You asked: {question}"}