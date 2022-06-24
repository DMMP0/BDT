# docker build -t bdt/ingestion-layer .

# docker run -d --name 1-Ingestion-Layer-BDT --network app-tier bdt/ingestion-layer

FROM python:latest
LABEL Mantainer1="huma.rehman@studenti.unitn.it", Mantainer2="maurizio.demarchi@studenti.unitn.it", Mantainer3="stefano.moro@studenti.unitn.it"

# set working directory,
WORKDIR /user/app/scr/BDT/Ingestion

# install libraries
RUN pip install kafka-python

RUN pip install redis

ADD main.py .
ADD services/ services/
ADD models/ models/
ADD components/ components/

CMD ["python","./main.py"]