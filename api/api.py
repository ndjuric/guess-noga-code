#!/usr/bin/env python
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from predictor import Predictor


class PredictorFactory(object):
    def __init__(self, description):
        self.description = description
        self.predicted = []

    def get_prediction(self, n):
        predictor[n].set_desc(self.description)
        predictor[n].tokenize()
        predictor[n].generate()
        predicted = predictor[n].run()
        predicted = [x for x in predicted if x.isdigit()]
        if len(predicted) > 0:
            self.predicted = predicted
        return predicted

    def run(self):
        sorted_keys = sorted(ngrams, reverse=True)
        for ngram in sorted_keys:
            predicted = self.get_prediction(ngram)
            if len(predicted) > 0:
                break
        return self.predicted


class Predict(Resource):
    def get(self):
        data = parser.parse_args()
        if not data['description']:
            return 'error'
        else:
            factory = PredictorFactory(data['description'])
            predicted = factory.run()
            print predicted
            return predicted


if __name__ == '__main__':
    ngrams = {
        1: '../ngrams/1.gram',
        2: '../ngrams/2.gram',
        3: '../ngrams/3.gram'
    }

    predictor = {}

    for n, db_name in ngrams.iteritems():
        predictor[n] = Predictor(db_name, n)
        print '{0}-grams db loaded.'.format(n)

    app = Flask(__name__)
    api = Api(app)

    parser = reqparse.RequestParser()
    parser.add_argument('description')
    api.add_resource(Predict, '/guess/')

    @app.route('/')
    def home(name=None):
        return render_template('index.html', name=name)

    app.run(host='0.0.0.0', port=1990)
