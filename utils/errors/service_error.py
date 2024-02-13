from fastapi import HTTPException

class ServiceError(HTTPException):
    def __init__(self, code: str, message: str, traceId: str, flightRecorder: dict, statusCode: int):
        self.code = code
        self.message = message
        self.traceId = traceId
        self.flightRecorder = flightRecorder
        super().__init__(detail=self.get_error_response(), status_code=statusCode)

    def get_error_response(self):
        return {
            "code": self.code,
            "message": self.message,
            "traceId": self.traceId,
            "flightRecorder": self.flightRecorder
        }