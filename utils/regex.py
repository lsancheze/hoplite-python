import re

TEMPLATE_ID_REGEX = r"^urn:[0-9a-fA-F]{24}:[0-9a-fA-F]{24}$"
RESOURCE_ID_REGEX = r"^urn:[0-9a-fA-F]{24}:[0-9a-fA-F]{24}$"
NAME_REGEX = r"^[a-zA-Z0-9-]{3,64}$"
DESCRIPTION_REGEX = r"^.{5,512}$"