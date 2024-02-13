import time
from functools import wraps
from utils.errors.service_error import ServiceError

def route_middleware(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Here you could do whatever operation you need to do across all the services
            try:
                response = await func(*args, **kwargs)
            except ServiceError as error:    
                raise error
            except Exception as error:
                # You could raise a different error if you need it
                raise error
            return response
        
        return wrapper
