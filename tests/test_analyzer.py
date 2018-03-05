import unittest
from analyzer.paragraph_analyzer import ParagraphAnalyzer


class TestParagraphAnalyzerMethods(unittest.TestCase):

    def setUp(self):
        self.text = "Fish fishes fishes. Fish. Another sentence. Last sentence with fishes."
        self.paragraph_analyzer = ParagraphAnalyzer()

    def test_get_unique_words(self):
        words = self.paragraph_analyzer.get_unique_words(self.text)
        self.assertEqual(6, len(words))
        self.assertEqual(4, words["fish"]["total-occurrences"])
        self.assertEqual({0, 1, 3}, words["fish"]["sentence-indexes"])

    def test_convert_words_dictionary_to_json(self):
        words = self.paragraph_analyzer.get_unique_words(self.text)
        json_result = self.paragraph_analyzer.convert_words_dictionary_to_json(words)
        expected_result = '''
        {
            "word": "fishes",
            "total-occurrences": 1,
            "sentence-indexes": [
                0
            ]
        },
        '''
        self.assertTrue(expected_result in json_result)


if __name__ == '__main__':
    unittest.main()
