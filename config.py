from dotenv import load_dotenv
import os

load_dotenv()

environment = "dev"
clinician_data = os.getenv('CLINICIAN_DATA')

if environment == "dev":
    origins = [os.getenv('DEV_ORIGIN')]
    mongo_client = os.getenv("MONGO_LOCAL_CLIENT")

elif environment == "qa":
    origins = [os.getenv('QA_ORIGIN')]

elif environment == "prod":
    origins = [os.getenv('PROD_ORIGIN')]

