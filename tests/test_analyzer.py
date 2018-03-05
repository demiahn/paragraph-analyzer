import unittest
from analyzer.paragraph_analyzer import ParagraphAnalyzer


class TestStringMethods(unittest.TestCase):

    def test_get_unique_words(self):
        text = "u Fish fishes fish fishes. Fish. Another sentence. Last sentence with fishes."
        paragraph_analyzer = ParagraphAnalyzer()
        words = paragraph_analyzer.get_unique_words(text)
        self.assertEqual(5, len(words))
        self.assertEqual(6, words["fish"]["total-occurrences"])
        self.assertEqual({0,1,3}, words["fish"]["sentence-indexes"])

if __name__ == '__main__':
    unittest.main()
