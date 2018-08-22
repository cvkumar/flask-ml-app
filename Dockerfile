# Format: FROM    repository[:version]
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

ADD ./requirements.txt ./app/requirements.txt
WORKDIR /app
RUN pip install -r ./requirements.txt
COPY . .

EXPOSE 5000

CMD python app/app.py