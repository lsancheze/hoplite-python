from fastapi import HTTPException
from utils.errors.service_error import ServiceError

async def get_template():
    # Your logic for handling the GET operation
    return {"message": "Hello World"}