from model import Clinician
import motor.motor_asyncio as mt
import config

client = mt.AsyncIOMotorClient(config.mongo_client)
database = client.MedicaidFinder
collection = database.clinician

async def get_all():
    clinicians = []
    cursor = collection.find({})
    async for document in cursor:
        clinicians.append(Clinician(**document))
    return clinicians

async def refresh_clinicians(clinician_list):
    await collection.delete_many({})
    documents = clinician_list
    result = await collection.insert_many(documents)
    return result
