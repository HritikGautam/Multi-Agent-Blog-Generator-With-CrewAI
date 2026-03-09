import os
from fastapi import FastAPI
from pydantic import BaseModel
from crew import blog_crew
from fastapi.middleware.cors import CORSMiddleware
# import litellm


os.environ["LITELLM_LOG"] = "INFO"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    # allow_origins=[
    #     "http://localhost:5500",
    #     "http://127.0.0.1:5500"
    # ],
    # allow_methods=["POST"],
    # allow_headers=["Content-Type"],
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class BlogRequest(BaseModel):
    topic: str
    
@app.get("/")
def home():
    return {"message" : "Crew AI!"}

@app.post("/generate-blog")
def generate_blog(request: BlogRequest):
    result = blog_crew.kickoff(inputs={"topic": request.topic})
    return {"result": str(result)}

if __name__ == "__main__":
    home() 



