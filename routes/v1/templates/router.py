from fastapi import APIRouter
from pydantic import BaseModel
from middlewares.route import route_middleware
from services.templates.get import get_template
from services.templates.create import create_template
from .entity import Template

router = APIRouter()

@router.get("/")
@route_middleware
async def root():
    return await get_template()

@router.post("/")
@route_middleware
async def root(payload: Template):
    return await create_template(payload)