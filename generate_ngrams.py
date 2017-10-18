import sys
from sentence import Sentence
from db import DB
from config import db_params


def most_common(l, n):
    counter = {}
    for x in l:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1

    common = sorted(counter, key=counter.get, reverse=True)
    return common[:n]


def main(n):
    db = DB(db_params)
    result = db.query(
        'select activityDescription,noga1,noga2,noga3,noga4,noga5 from CONTACTS where noga1!="" AND '
        'activityDescription != "N/A" limit 10000'
    )

    knowledge = {}
    for item in result:

        description = item[0].lower()
        nogas = [item[1], item[2], item[3], item[4], item[5]]
        nogas = filter(None, nogas)
        noga = str(nogas[0])

        sentence_proc = Sentence(n)
        sentence_proc.set_desc(description)
        sentence_proc.tokenize()
        sentence_proc.generate_ngrams()

        all_ngrams = sentence_proc.get_ngrams()

        for ngram in all_ngrams:
            if ngram not in knowledge:
                knowledge[ngram] = []
            knowledge[ngram].append(noga)

    for key, value in knowledge.iteritems():
        value = most_common(value, 5)
        value = ', '.join(value)
        print '{0}, {1}'.format(key, value)


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
