FROM python:3.11-slim

RUN useradd -ms /bin/bash python

USER python

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src

WORKDIR /home/python/app

CMD [ "tail","-f","/dev/null" ]

