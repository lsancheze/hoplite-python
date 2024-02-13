from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.exceptions import RequestValidationError
from routes.v1.setup import setup
from middlewares.error import http_exception_handler, validation_exception_handler

app = FastAPI()

# Create an instance of APIRouter to group all routers
v1Router = APIRouter()

# Include all routers from the v1 directory using the setup function
setup(v1Router)

# Include the grouped router in your app
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.include_router(v1Router, prefix="/v1", tags=["v1"])
