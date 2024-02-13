from fastapi.responses import JSONResponse
# from fastapi import HTTPException, RequestValidationError

def http_exception_handler(request, error):
    return JSONResponse(
        content={
            "code": error.code,
            "message": error.message,
            "traceId": error.traceId,
            "flightRecorder": error.flightRecorder
        },
        status_code=error.status_code
    )

def validation_exception_handler(request, error):
    return JSONResponse(content={
        "code": "invalid-request",
        "message": f"{error.errors()[0]['msg']} at {error.errors()[0]['loc']}"
        },
        status_code=422
    )