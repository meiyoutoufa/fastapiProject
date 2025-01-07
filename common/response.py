
from typing import Any
from pydantic import BaseModel


class Response(BaseModel):
    code: int
    data: Any = None
    message: str = None

def success_data(data: Any) -> Response:
    return Response(code=200, data=data, message='success')


def failure(code: int, message: str)->Response:
    return Response(code=code, message=message, data=None)
