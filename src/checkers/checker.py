from typing import Protocol, Callable, Any

from src.file import File


class Checker(Protocol):
    def validate(self,file:File,callback:Callable[..., Any], *args: Any) -> bool:
        pass