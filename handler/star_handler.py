from typing import Any

from handler.abstract_handler import AbstractHandler

class StarHandler(AbstractHandler):
    """
        Concrete implementation of a handler for matching star characters.
    """

    def handle(self, pattern_position: Any, pattern_string: Any, target_position: Any, target_string: Any) -> int:
        """
        Matches a star character in the pattern with 0 or more characters in target string
        :param pattern_position: character position of pattern
        :param pattern_string: pattern to be matched
        :param target_position: character position of target string
        :param target_string: string to be matched
        :return: position of matched character, -1 if no match found or end of string reached
        """
        print(("star handler", pattern_position, pattern_string, target_position, target_string))
        if pattern_string[pattern_position] == '*':
            #looping till we get the next character in target string
            for target_index, ch in enumerate(target_string[target_position:], start=target_position):
                if int(pattern_position) + 1 < len(pattern_string) and int(target_position) + 1 < len(target_string):
                    # Check the next handler if match found
                    matched = super().handle(pattern_position+1, pattern_string, target_index, target_string)
                    if matched == -1:
                        continue
                    else:
                        return target_position - 1
        else:
            return -1
