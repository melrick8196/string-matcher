
from handler.handler import Handler
from handler.char_handler import CharHandler
from handler.dot_handler import DotHandler
from handler.star_handler import StarHandler
from handler.abstract_handler import AbstractHandler
from match import Match

def make_pattern():
    head = CharHandler()
    c = CharHandler()
    d = DotHandler()
    t = CharHandler()
    head.set_next(StarHandler()).set_next(CharHandler())
    print(head)
    user_pattern = "c.t"
    user_target_string = "act"
    print("pattern:{}, target_string:{}".format(user_pattern, user_target_string))
    res = client_code(head)
    print("final res:",res)

def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """
    user_pattern = "c*t"
    user_target_string = "xxxxcat"
    pattern_pos = 0
    target_string_pos = 0
    for index, ele in enumerate(user_target_string):
        print(f"\nClient: Who wants a {ele}?")
        result = handler.handle(pattern_pos, user_pattern, index, user_target_string)
        print(result)
        if result == -1 and index < len(user_target_string):
            continue
        else:
            break
    return result


if __name__ == "__main__":
    #x = Match("c.t")
    #x.find_first_ln("ffffffffffffffack")
    make_pattern()
