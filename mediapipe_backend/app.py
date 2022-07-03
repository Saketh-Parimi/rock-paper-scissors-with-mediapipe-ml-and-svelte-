from flask import Flask, request
from flask_cors import CORS
from joblib import load
import numpy as np

# csv = pandas.read_csv('./rps.csv')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def home():
  m = load('../model.jlb')
  y_predict = m.predict([request.json['body']['landmarks']])
  return {'class': int(y_predict)}

if __name__ == '__main__':
  app.run(debug=True)