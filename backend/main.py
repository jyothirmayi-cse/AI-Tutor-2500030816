from fastapi import FastAPI

klu = FastAPI(title="AI Tutor",
              description="AI Tutor pbl project",
              version="1.0.0")

@klu.get("/")
def home():
    return {"message" : "welcome to AI Tutor project"}

@klu.get("/demo")
def demo():
    return {"message" : "KL University"}

@klu.get("/askquestion")
def ask():
    return {"message" : "What is LLM", "Answer" : "Large Language Model"}

@klu.get("/emp")
def emp():
    return {"id" : 1, "name" : "Ram", "gender" : "Male", "course" : "DSA"}

@klu.get("/students")
def getstudents():
    return [{"id" : 1, "name" : "Ram", "gender" : "Male", "course" : "DSA"},
            {"id" : 2, "name" : "Sita", "gender" : "Female", "course" : "DSA"},
            {"id" : 3, "name" : "Ravan", "gender" : "Male", "course" : "DSA"}
            ]