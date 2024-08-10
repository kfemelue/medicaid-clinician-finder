from dotenv import load_dotenv
import os

load_dotenv()

environment = "dev"
clinician_data = os.getenv('CLINICIAN_DATA')
national_downloadable_file = os.getenv('NATIONAL_DOWNLOADABLE_FILE')

if environment == "dev":
    origins = [os.getenv('DEV_ORIGIN')]
    mongo_client = os.getenv("MONGO_LOCAL_CLIENT")

elif environment == "qa":
    origins = [os.getenv('QA_ORIGIN')]
    mongo_client = os.getenv("MONGO_QA_CLIENT")

elif environment == "prod":
    origins = [os.getenv('PROD_ORIGIN')]
    mongo_client = os.getenv("MONGO_PROD_CLIENT")

