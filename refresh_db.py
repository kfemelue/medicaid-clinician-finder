import config
import requests
import database
import asyncio
import pandas as pd
from model import Clinician
from requests.exceptions import HTTPError, Timeout, RequestException
from io import StringIO


async def get_clinicians():
    # external_api_url = config.clinician_data
    data_url = config.national_downloadable_file
    try:
        print("Fetching Data")
        # responses = requests.get(external_api_url)
        # data = responses.json()
        # data_list = data['results']
        #
        # for item in data_list:
        #     clinician = Clinician(**item)
        #     item = clinician.dict()
        #
        # await database.refresh_clinicians(data_list)

        # variable 'responses' contains the full data.cms.gov national_downloadable_file csv
        responses = requests.get(data_url)
        ndf_df = pd.read_csv(StringIO(responses.text), dtype=str)
        documents = ndf_df.to_dict(orient='records')

        print("Loading data into Collection")

        await database.refresh_clinicians(documents)

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
        print("Collection Update Complete")


asyncio.run(get_clinicians())
