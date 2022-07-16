# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle

app = Flask(__name__)
api = Api(app)

class RawFeats:
    def __init__(self, feats):
        self.feats = feats

    def fit(self, X, y=None):
        pass

    def transform(self, X, y=None):
        return X[self.feats]

    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)
    
model = pickle.load(open("log_reg.pkl", "rb"))

class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        print(df)
        # # getting predictions from our model.
        # it is much simpler because we used pipelines during development
        res = model.predict(df).tolist()
        print(res)
        response_dict = {'response': res}
        # we cannot send numpt array as a result
        return jsonify(response_dict) 

    
# assign endpoint
api.add_resource(Scoring, '/scoring',)

if __name__ == '__main__':
    app.run(debug=True, port=8000)