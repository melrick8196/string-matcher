from handler.handler import Handler
from abc import abstractmethod
from typing import Any


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Used for creating a chain of handlers

        return handler


    @abstractmethod
    def handle(self, pattern_position: Any, pattern_string: Any, target_position: Any, target_string: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(pattern_position, pattern_string, target_position, target_string)

        return None
