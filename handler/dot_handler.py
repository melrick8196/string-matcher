from typing import Any

from handler.abstract_handler import AbstractHandler

class DotHandler(AbstractHandler):
    """
        Concrete implementation of a handler for matching dot characters.
    """

    def handle(self, pattern_position: Any, pattern_string: Any, target_position: Any, target_string: Any) -> int:
        """
        Matches a dot character in the pattern with any character in target string
        :param pattern_position: character position of pattern
        :param pattern_string: pattern to be matched
        :param target_position: character position of target string
        :param target_string: string to be matched
        :return: position of matched character, -1 if no match found or end of string reached
        """
        print(("dot handler", pattern_position, pattern_string, target_position, target_string))
        if pattern_string[pattern_position] == '.':
            if int(pattern_position) + 1 < len(pattern_string) and int(target_position) + 1 < len(target_string):
                pattern_position += 1
                target_position += 1
                # Check the next handler if match found
                matched = super().handle(pattern_position, pattern_string, target_position, target_string)
                if matched == -1:
                    return -1
                else:
                    return target_position - 1
            else:
                print("Length exceded for pattern and string")
                return target_position - 1
        else:
            return -1

