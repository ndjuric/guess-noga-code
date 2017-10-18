class Predictor(object):
    def __init__(self, db_file, n):
        self.db_file = db_file
        self.knowledge = {}
        self.description = ''
        self.tokens = []
        self.ngrams = set()
        self.N = n

        for line in open(db_file).read().splitlines():
            data = line.split(', ')
            word = data[0]
            self.knowledge[word] = []
            for i in range(1, len(data)):
                self.knowledge[word].append(data[i])

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

    def generate(self):
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

    def run(self):
        nogas = []
        for ngram in self.ngrams:
            # print(ngram)
            if ngram in self.knowledge:
                # print(self.knowledge[ngram])
                nogas.append(self.knowledge[ngram])
            else:
                print "nothing found"

        flat_list = {}
        for sublist in nogas:
            for item in sublist:
                if item not in flat_list:
                    flat_list[item] = 0
                else:
                    flat_list[item] += 1

        return sorted(flat_list, key=flat_list.get, reverse=True)
