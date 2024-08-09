import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# App Object to create fast API app
app = FastAPI()
environment = "dev"
if environment == "dev":
    origins = [os.getenv('DEV_ORIGINS')]
elif environment == "qa":
    origins = [os.getenv('QA_ORIGINS')]
elif environment == "prod":
    origins = [os.getenv('PROD_ORIGINS')]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Ping": "Pong"}