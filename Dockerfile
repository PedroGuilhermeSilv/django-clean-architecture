FROM python:3.11-slim

RUN apt update && apt install -y --no-install-recommends default-jre git

RUN useradd -ms /bin/bash python

USER python

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

WORKDIR /home/python/app

CMD [ "tail","-f","/dev/null" ]

