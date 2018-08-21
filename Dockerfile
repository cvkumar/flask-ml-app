# Format: FROM    repository[:version]
FROM       ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /flask-ml-app
WORKDIR /flask-ml-app

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app/app.py"]