import unittest
from handler.handler import Handler
from handler.char_handler import CharHandler
from handler.dot_handler import DotHandler
from handler.star_handler import StarHandler
from handler.abstract_handler import AbstractHandler
from match import Match

class MatchTest(unittest.TestCase):
    def match_pattern(self):
        match = Match("c*t")
        self.assertEqual(0, match.find_first_ln("cacacat"))

        match = Match("c.t")
        self.assertEqual(4, match.find_first_ln("xxxxcat"))

        match = Match("c..t")
        self.assertEqual(2, match.find_first_ln("xxcaatxxxx"))

        match = Match("abc.t")
        self.assertEqual(2, match.find_first_ln("xxabcatxxxx"))

        match = Match("c*tb")
        self.assertEqual(2, match.find_first_ln("bacatatb"))



if __name__ == "__main__":
    m = MatchTest()
    m.match_pattern()