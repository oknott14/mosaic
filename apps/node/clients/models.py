from typing import Generic, TypeVar

from pydantic import BaseModel


class HttpResponse(BaseModel):
    status: int


T = TypeVar("T", bound=BaseModel)


class HttpPostResponse(HttpResponse, Generic[T]):
    body: T
