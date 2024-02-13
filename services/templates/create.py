from utils.errors.service_error import ServiceError
from routes.v1.templates.entity import Template

async def create_template(payload: Template):
    if payload.age > 1:
        raise ServiceError(
            code="teapot-error",
            message="Nope! I don't like that.",
            traceId="optional",
            flightRecorder={"key": "value"},
            statusCode=418
        )
    return {"message": payload.age}