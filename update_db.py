import os
import requests
from requests.exceptions import HTTPError, Timeout, RequestException


def get_clinicians(self):
    external_api_url = os.getenv("CLINICIAN_DATA")
    try:
        responses = requests.get(external_api_url)
        data = responses.json()
        return data

    except HTTPError as http_error:
        return f"HTTP Error: {http_error}"

    except Timeout as timeout_error:
        return f"HTTP Error: {timeout_error}"

    except RequestException as request_error:
        return f"HTTP Error: {request_error}"

    except Exception as exception:
        return f"HTTP Error: {exception}"

