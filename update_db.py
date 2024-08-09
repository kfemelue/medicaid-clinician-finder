import os
import requests
import database
from model import Clinician
from requests.exceptions import HTTPError, Timeout, RequestException


def get_clinicians(self):
    external_api_url = os.getenv("CLINICIAN_DATA")
    try:
        responses = requests.get(external_api_url)
        data = responses.json()

        for item in data:
            clinician = Clinician(**item)
            document = clinician.dict()
            database.create_clinician(document)
            
        print("Database Update Complete")

    except HTTPError as http_error:
        return f"HTTP Error: {http_error}"

    except Timeout as timeout_error:
        return f"HTTP Error: {timeout_error}"

    except RequestException as request_error:
        return f"HTTP Error: {request_error}"

    except Exception as exception:
        return f"HTTP Error: {exception}"
