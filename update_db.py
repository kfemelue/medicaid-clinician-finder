import config
import requests
import database
import asyncio
from model import Clinician
from requests.exceptions import HTTPError, Timeout, RequestException


async def get_clinicians():
    external_api_url = config.clinician_data
    try:
        print("Fetching Data")
        responses = requests.get(external_api_url)
        data = responses.json()

        for item in data['results']:
            clinician = Clinician(**item)
            document = clinician.dict()
            await database.create_clinician(document)

    except HTTPError as http_error:
        print(f"HTTP Error: {http_error}")
        return f"HTTP Error: {http_error}"

    except Timeout as timeout_error:
        print(f"Timeout Error: {timeout_error}")
        return f"Timeout Error: {timeout_error}"

    except RequestException as request_error:
        print(f"Request Error: {request_error}")
        return f"Request Error: {request_error}"

    except Exception as exception:
        print(f"Exception: {exception}")
        return f"Exception: {exception}"
    
    finally:
        print("Database Update Complete")


asyncio.run(get_clinicians())