# flask-ml-app

A simple application that enables a user to train a support vector machine (svm) model on 
the classical [Iris Flower Dataset](https://archive.ics.uci.edu/ml/datasets/iris) and use it to predict the classification of a flower based on sepal length, sepal width, petal length, and petal width.

UI: Angular 6 <br />
Backend: Python Flask <br />
ORM: PonyORM <br />
Database: Postgres

You can watch a demo of the app running with:
`demo.mov`

## Getting Started

First fork or clone this repo:

i.e. git clone https://github.com/cvkumar/flask-ml-app.git


To run the app locally:

```
docker-compose up --build app
```
and
```
cd frontend/my-app

npm install
npm start
```

Go to http://localhost:4200.


## Prerequisites

Using [brew](https://brew.sh/):
```
brew install node
brew install angular-cli
```
Also install: <br />
-[Docker](https://docs.docker.com/install/) <br />
-[Docker-compose](https://docs.docker.com/compose/install/)

## Future Features

- Run Angular application paired with docker-compose using NGINX
- Expose API for inputting training/test data
- Create user inputs for SVM model hyperparameters and training/test data split 
- Improve UI with Angular Material Components

## Authors

* **Caleb Kumar** - [cvkumar](https://github.com/cvkumar)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

