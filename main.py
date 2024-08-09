import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# App Object to create fast API app
app = FastAPI()
environment = "dev"
if environment == "dev":
    origins = [os.getenv('DEV_ORIGIN')]
elif environment == "qa":
    origins = [os.getenv('QA_ORIGIN')]
elif environment == "prod":
    origins = [os.getenv('PROD_ORIGIN')]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def get_homepage():
    return {"Ping": "Pong"}


@app.get("/api/clinicians")
async def get_clinicians():
    return 1


@app.get("/api/clinician/id")
async def get_clinician():
    return 1
