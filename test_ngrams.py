import sys
from config import ngrams_dir
from sentence import Sentence
from db import DB
from config import db_params


class SentenceNoga(Sentence):
    def __init__(self, n):
        Sentence.__init__(self, n)
        self.knowledge = {}

        for line in open(ngrams_dir + str(n) + '.gram').read().splitlines():
            data = line.split(', ')
            word = data[0]
            self.knowledge[word] = []
            for i in range(1, len(data)):
                self.knowledge[word].append(data[i])

    def run(self):
        nogas = []
        for ngram in self.ngrams:
            if ngram in self.knowledge:
                nogas.append(self.knowledge[ngram])
            else:
                print "nothing found"

        flat_list = {}
        for sublist in nogas:
            for list_item in sublist:
                if list_item not in flat_list:
                    flat_list[list_item] = 0
                else:
                    flat_list[list_item] += 1
        return sorted(flat_list, key=flat_list.get, reverse=True)


def percentage(part, whole):
    return 100 * float(part) / float(whole)


def main(n):
    total = 0
    first_matches = 0
    group_of_three_matches = 0
    predictor = SentenceNoga(n)
    db = DB(db_params)
    result = db.query('select activityDescription,noga1,noga2,noga3,noga4,noga5 from CONTACTS limit 10000 offset 700000')
    for item in result:
        description = item[0]
        nogas = [item[1], item[2], item[3], item[4], item[5]]
        nogas = filter(None, nogas)

        predictor.set_desc(description)
        predictor.tokenize()
        predictor.generate_ngrams()
        predicted = predictor.run()
        predicted = [x for x in predicted if x.isdigit()]

        print description
        print nogas
        print predicted[:3]
        print '-'
        if len(predicted) > 0 and len(nogas) > 0:
            proba = list(set(nogas).intersection(predicted[:3]))
            if len(proba) > 0:
                group_of_three_matches += 1

            if nogas[0] == predicted[0]:
                first_matches += 1
            total += 1

    print 'First predicted NOGA is a match: {0}/{1} ({2}%)'.format(
        first_matches, total, str(round(percentage(first_matches, total), 2)))

    print 'One NOGA from group of first 3 predicted is a match: {0}/{1} ({2}%)'.format(
        group_of_three_matches, total, str(round(percentage(group_of_three_matches, total), 2))
    )


def is_numeric(n):
    try:
        val = int(n)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    args = sys.argv[1:]
    args_len = len(args)
    if (args_len > 1) or (args_len < 1) or (not is_numeric(args[0])):
        print('example: python {0} 3'.format(sys.argv[0]))
        exit()

    n = int(args[0])
    main(n)
