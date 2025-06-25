from abc import ABC
from os import environ
from typing import Callable, TypeVar

from decorators.singleton import singleton


class UnknownEnvironmentVariableError(Exception):
    def __init__(self, var: str) -> None:
        super().__init__(f"Unknown Environment Variable `{var}`")


T = TypeVar("T")


@singleton
class Environment(ABC):
    def get(self, var: str, cast_to: Callable[[str], T] = str) -> T | None:
        if var in environ:
            return cast_to(environ[var])
        else:
            return None

    def get_or_default_to(
        self, var: str, default: T, cast_to: Callable[[str], T] = str
    ) -> T:
        env_var = self.get(var, cast_to)

        if env_var is None:
            return default

        return env_var

    def get_or_throw(self, var: str, cast_to: Callable[[str], T] = str) -> T:
        env_var = self.get(var, cast_to)

        if env_var is None:
            raise UnknownEnvironmentVariableError(var)

        return env_var
