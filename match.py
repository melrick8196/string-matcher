from handler.handler import Handler
from handler.char_handler import CharHandler
from handler.dot_handler import DotHandler
from handler.star_handler import StarHandler
from handler.abstract_handler import AbstractHandler

class Match():
    """
    Class for creating a pattern chain using a chain of handlers.
    """
    def __init__(self, pattern: str):
        """
        Recursively calling the handler classes for creating chain
        :param pattern:
        """
        self.user_pattern = pattern
        character = CharHandler()
        dot = DotHandler()
        star = StarHandler()

        if pattern[0].isalpha():
            self.head = CharHandler()
        if pattern[0] == '*':
            self.head = StarHandler()
        if pattern[0] == '.':
            self.head = DotHandler()

        for character in pattern[1:]:
            if character.isalpha():
                self.head = self.head.set_next(CharHandler())
            if pattern[0] == '*':
                self.head = self.head.set_next(StarHandler())
            if pattern[0] == '.':
                self.head = self.head.set_next(DotHandler())

    def find_first_ln(self, user_target_string: str) -> int:

        pattern_pos = 0
        for index, ele in enumerate(user_target_string):
            print("Element being checked: {}".format(ele))
            result = self.head.handle(pattern_pos, self.user_pattern, index, user_target_string)
            print(result)
            if result == -1 and index < len(user_target_string):
                continue
            else:
                break
        return result