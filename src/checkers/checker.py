from typing import Protocol, Callable, Any

from src.file import File


class Checker(Protocol):
    """Protocol for file checkers that validate files and trigger callbacks."""
    def validate(self,file:File,callback:Callable[..., Any], *args: Any) -> bool:
        """Validate the file and optionally invoke a callback if validation passes."""
        pass