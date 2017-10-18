#!/usr/bin/env python


class Sentence(object):
    def __init__(self, n):
        self.description = ''
        self.tokens = []
        self.ngrams = set()
        self.N = n

    def set_desc(self, description):
        description = description.lower()
        description = description.rstrip()
        description = description.replace('\'', '')
        description = description.replace('\"', '')
        description = description.replace(',', '')
        description = description.replace('.', '')
        description = description.replace('-', '')
        description = description.replace('/', ' ')
        description = description.replace('\\', '')
        description = description.replace('(', '')
        description = description.replace(')', '')
        description = description.replace(';', '')
        self.description = description

    def tokenize(self):
        desc_split = self.description.split(' ')

        tokens = []
        for token in desc_split:
            if len(token) > 4:
                tokens.append(token)
        self.tokens = []
        self.tokens = tokens

    def generate_ngrams(self):
        self.ngrams = set()
        for i in range(0, len(self.tokens) - self.N + 1):
            s = ""
            start = i
            end = i + self.N
            for j in range(start, end):
                s += ' ' + self.tokens[j]
            s = s.lstrip()
            s = s.rstrip()
            self.ngrams.add(s)

    def get_ngrams(self):
        return self.ngrams