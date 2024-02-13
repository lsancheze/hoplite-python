from fastapi import APIRouter
from .templates.router import router as templates_router
# Import other routers as needed

def setup(app: APIRouter):
    app.include_router(templates_router, prefix="/templates", tags=["templates"])
    # Include other routers as needed
