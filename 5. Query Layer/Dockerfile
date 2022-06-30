FROM python:latest
LABEL Mantainer1="huma.rehman@studenti.unitn.it", Mantainer2="maurizio.demarchi@studenti.unitn.it", Mantainer3="stefano.moro@studenti.unitn.it"

# set working directory,
WORKDIR /user/app/scr/BDT/Frontend

# install libraries
RUN pip install anvil
RUN pip install anvil-uplink
RUN pip install mysql
RUN pip install mysql-connector
RUN pip install dataclasses

ADD main.py .
ADD services/ services/
ADD models/ models/
ADD components/ components/

CMD ["stdbuf", "-oL","python","./main.py"]