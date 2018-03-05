import json
import spacy


class ParagraphAnalyzer:

    def __init__(self):
        self._excluded_words = []

    _excluded_part_of_speech = ["PUNCT", "SPACE"]

    @property
    def excluded_words(self):
        """List of excluded words"""
        return self._excluded_words

    @excluded_words.setter
    def excluded_words(self, value):
        self._excluded_words = value

    def get_unique_words(self, text):
        """Returns a dictionary of unique words for the paragraph containing the number of occurrences
        and the sentence index"""

        sentence = 0
        words = {}

        nlp = spacy.load('en')
        doc = nlp(text)

        for token in doc:
            if token.text == ".":
                sentence += 1

            if token.pos_ not in self._excluded_part_of_speech and token.lemma_ not in self._excluded_words:

                # Pronouns have -PROUN- as lemma so we keep their text name
                if token.lemma_ == "-PRON-":
                    word = token.text
                else:
                    word = token.lemma_

                if word in words:
                    words[word]["total-occurrences"] += 1
                    words[word]["sentence-indexes"].add(sentence)
                else:
                    words[word] = {"total-occurrences": 1, "sentence-indexes": set([sentence])}

        return words

    def convert_words_dictionary_to_json(self, words):
        """ Converts a words dictionary to json format"""

        ordered_words = []
        for key, value in sorted(words.items(), key=lambda v: v[0].upper()):
            ordered_words.append({"word": key, "total-occurrences": value["total-occurrences"],
                                  "sentence-indexes": list(value["sentence-indexes"])})

        results = {"results": ordered_words}

        return json.dumps(results, indent=4)
