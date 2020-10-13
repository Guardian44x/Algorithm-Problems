"""
$ Check If a Word Occurs As a Prefix of Any Word in a Sentence
"""

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        for i, c in enumerate(sentence):
            if len(c) < len(searchWord):
                continue
            l = len(searchWord)
            if c[:l] == searchWord:
                return i+1
        else:
            return -1