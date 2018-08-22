# Format: FROM    repository[:version]
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

ADD ./requirements.txt ./app/requirements.txt
WORKDIR /app
RUN pip install -r ./requirements.txt
COPY . .
#COPY . /app
#WORKDIR /app

EXPOSE 5000

#RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
CMD python app/app.py