from pydantic import BaseModel
from typing import Generic, Optional, TypeVar, Optional
from fastapi.responses import ORJSONResponse
from pydantic.dataclasses import dataclass

from app.models.dtos.common import PageDTO

T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    message: str = "OK"
    statusCode: str = "200"
    data: Optional[T] = None


class ErrorResponse(BaseModel):
    message: str
    statusCode: str


class HttpResponse(ORJSONResponse):
    def __init__(self, content: Optional[T] = None, **kwargs):
        super().__init__(
            content={
                "message": "OK",
                "statusCode": "200",
                "data": content,
            },
            **kwargs
        )
