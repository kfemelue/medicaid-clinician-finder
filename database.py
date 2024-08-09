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

async def create_clinician(Clinician):
    document = Clinician
    result = await collection.insert_one(document)
    return result
