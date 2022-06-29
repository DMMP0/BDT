# credentials=$(< ../credentials/db-config.json)
# docker build -t bdt/storage-layer .

# docker run -e "CREDENTIALS=$credentials" -d --name 4-Storage-Layer-BDT  --network app-tier bdt/storage-layer
# redis and sql container must run too

FROM python:latest
LABEL Mantainer1="huma.rehman@studenti.unitn.it", Mantainer2="maurizio.demarchi@studenti.unitn.it", Mantainer3="stefano.moro@studenti.unitn.it"

# set working directory,
WORKDIR /user/app/scr/BDT/Storage

# install libraries
RUN pip install redis
RUN pip install mysql
RUN pip install mysql-connector-python
RUN pip install mysql-client

ADD main.py .
ADD services/ services/
ADD models/ models/
ADD components/ components/

CMD ["stdbuf", "-oL","python","./main.py"]