from flask import Flask
from flask import request
from flask import jsonify

from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

app = Flask(__name__)


@app.route('/train')
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

    model_accuracy = svm_model.score(x_test, y_test)

    return jsonify({'success': True, 'model_accuracy': model_accuracy})


@app.route('/test')
def test_model():
    """
    TODO: Upload data to test accuracy

    :return:
    """
    return 'TODO'


@app.route('/predict', methods=['POST'])
def predict():
    # print(request.json)

    svm_model = joblib.load('model.pkl')

    flower = [
        [float(request.json['sepal_length']), float(request.json['sepal_width']), float(request.json['petal_length']),
         float(request.json['petal_width'])]]

    prediction = svm_model.predict_proba(flower)[0]
    response = jsonify({'Setosa': prediction[0], 'Versicolour': prediction[1], 'Virginica': prediction[2]})

    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
