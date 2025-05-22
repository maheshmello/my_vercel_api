from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks.json, which is a list of dicts
try:
    with open("q-vercel-python.json", "r") as f:
        marks_list = json.load(f)  # List of students
except Exception as e:
    print("Error loading marks.json:", e)
    marks_list = []

# Lookup function to find marks by name
def get_mark_for_name(name):
    for student in marks_list:
        if student.get("name") == name:
            return student.get("marks")
    return None

@app.get("/api")
def get_marks(request: Request):
    try:
        names = request.query_params.getlist("name")
        result = [get_mark_for_name(name) for name in names]
        return {"marks": result}
    except Exception as e:
        print("Error in /api:", e)
        return {"error": str(e)}
