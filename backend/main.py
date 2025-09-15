from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, Resume Job App!"}

@app.post("/signup")
def signup(email: str = Form(...), password: str = Form(...)):
    return {"email": email, "password": password}

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    with open(f"./{file.filename}", "wb") as f:
        f.write(contents)
    return {"filename": file.filename}
