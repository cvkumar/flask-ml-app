import os

from flask import Flask
from flask import request
from flask import jsonify

from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

from uuid import uuid4
from datetime import datetime

import pony.orm as pny

import database
import config

app = Flask(__name__)


@app.route('/train')
@pny.db_session
def train_model():
    iris_dataset = datasets.load_iris()
    X, y = iris_dataset.data, iris_dataset.target

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, stratify=y)

    # print(iris_dataset['DESCR'])

    # Fit Model
    svm_model = svm.SVC(
        C=1.0,
        probability=True,
        random_state=1)
    svm_model.fit(x_train, y_train)

    joblib.dump(svm_model, 'model.pkl')

    pny.delete(prediction for prediction in database.Prediction)

    model_accuracy = svm_model.score(x_test, y_test)

    return jsonify({'success': True, 'model_accuracy': model_accuracy})


@app.route('/predict', methods=['POST'])
@pny.db_session
def predict():
    # print(request.json)

    svm_model = joblib.load('model.pkl')

    sepal_length = float(request.json['sepal_length'])
    sepal_width = float(request.json['sepal_width'])
    petal_length = float(request.json['petal_length'])
    petal_width = float(request.json['petal_width'])

    flower = [[sepal_length, sepal_width, petal_length, petal_width]]

    prediction = __make_prediction(flower, svm_model)

    database.Prediction(id=unicode(str(uuid4())), date=datetime.now(), sepal_length=sepal_length,
                        sepal_width=sepal_width, petal_length=petal_length, petal_width=petal_width,
                        prediction=prediction)

    response = jsonify({"prediction": prediction})

    return response


@app.route('/predictions', methods=['GET'])
@pny.db_session
def get_predictions():
    predictions = database.Prediction.select().order_by(pny.desc(database.Prediction.date))[:]
    response = jsonify({'predictions': [prediction.to_dict() for prediction in predictions]})
    return response


@app.route('/predictions', methods=['DELETE'])
@pny.db_session
def clear_predictions():
    pny.delete(prediction for prediction in database.Prediction)
    return jsonify({'success': True})


def __make_prediction(flower, svm_model):
    predictions = svm_model.predict_proba(flower)[0]
    result = {'Setosa': predictions[0], 'Versicolour': predictions[1], 'Virginica': predictions[2]}
    if result['Setosa'] >= result['Versicolour'] and result['Setosa'] > result['Versicolour']:
        return 'Setosa'
    elif result['Versicolour'] >= result['Setosa'] and result['Versicolour'] > result['Virginica']:
        return 'Versicolour'
    else:
        return 'Virginica'


if __name__ == "__main__":
    if os.environ["LOCAL"] == "True":
        config.set_private_environment_variables()

    database.connect_database()

    app.run(debug=True, host='0.0.0.0')
