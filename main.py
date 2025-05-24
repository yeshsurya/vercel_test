# main.py
import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from q-vercel-python.json
with open("q-vercel-python.json", "r") as f:
    marks_list = json.load(f)
marks_data = {item["name"]: item["marks"] for item in marks_list}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def get_marks(name: list[str] = Query(default=[])):
    marks = [marks_data.get(n, 0) for n in name]
    return {"marks": marks}