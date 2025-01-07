
from pydantic import BaseModel, field_validator


class UserRequest(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls, value):
        assert value.isalnum(), 'nanananan'
        return value


class UserResponse(BaseModel):
    username: str
