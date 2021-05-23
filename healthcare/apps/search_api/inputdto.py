from pydantic import BaseModel, validator, ValidationError


class SearchDTO(BaseModel):
    page: int = 0
    keyword: str = None
