from analyzer.paragraph_analyzer import ParagraphAnalyzer

paragraph_analyzer = ParagraphAnalyzer()

paragraph_analyzer.excluded_words = ["a", "the", "and", "of", "in", "be", "also", "as"]

text = "uTake this paragraph of text and return an alphabetized list of ALL unique words." \
       "  A unique word is any form of a word often communicated with essentially the same meaning." \
       " For example, fish and fishes could be defined as a unique word by using their stem fish." \
       " For each unique word found in this entire paragraph, determine the how many times the word appears in total." \
       " Also, provide an analysis of what unique sentence index position or positions the word is found." \
       " The following words should not be included in your analysis or result set: \"a\", \"the\", \"and\", \"of\", \"in\", \"be\", \"also\" and \"as\"." \
       "  Your final result MUST be displayed in a readable console output in the same format as the JSON sample object shown below."

words = paragraph_analyzer.get_unique_words(text)

json_result = paragraph_analyzer.convert_words_dictionary_to_json(words)

print(json_result)
