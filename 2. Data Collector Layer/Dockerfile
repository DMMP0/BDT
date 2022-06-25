# credentials=$(< ../credentials/bdt-project-200-6164fe338b7d.json)
# docker build -t bdt/collector-layer .

# docker run -d --name 2-Collector-Layer-BDT -e $credentials --network app-tier bdt/collector-layer

FROM python:latest
LABEL Mantainer1="huma.rehman@studenti.unitn.it", Mantainer2="maurizio.demarchi@studenti.unitn.it", Mantainer3="stefano.moro@studenti.unitn.it"

# set working directory,
WORKDIR /user/app/scr/BDT/Collector

# install libraries
RUN pip install kafka-python
RUN pip install google
RUN pip install google-api-core
RUN pip install google-auth
RUN pip install google-cloud-storage

ADD main.py .
ADD services/ services/
ADD models/ models/
ADD components/ components/

CMD ["python","./main.py"]