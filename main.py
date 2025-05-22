from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the marks.json file
try:
    with open("q-vercel-python.json", "r") as f:
        marks_dict = json.load(f)
except Exception as e:
    print("Failed to load marks.json:", e)
    marks_dict = {}

@app.get("/api")
def get_marks(request: Request):
    try:
        names = request.query_params.getlist("name")
        print("Received names:", names)
        result = [marks_dict.get(name, None) for name in names]
        return {"marks": result}
    except Exception as e:
        print("Error in /api:", e)
        return {"error": str(e)}
