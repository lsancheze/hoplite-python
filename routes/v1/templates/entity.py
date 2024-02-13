from pydantic import BaseModel, Field
from utils.regex import RESOURCE_ID_REGEX, NAME_REGEX, DESCRIPTION_REGEX
class Template(BaseModel):
    resourceId: str = Field(pattern=RESOURCE_ID_REGEX)
    description: str = Field(pattern=DESCRIPTION_REGEX)
    name: str = Field(pattern=NAME_REGEX)
    age: int