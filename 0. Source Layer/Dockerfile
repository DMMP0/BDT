FROM python:latest
LABEL Mantainer1="huma.rehman@studenti.unitn.it", Mantainer2="maurizio.demarchi@studenti.unitn.it", Mantainer3="stefano.moro@studenti.unitn.it"

# set working directory,
WORKDIR /user/app/scr

# install libraries
RUN pip install pandas
RUN pip install uuid
RUN pip install numpy
RUN pip install docx
RUN pip install kafka

ADD main.py .
ADD services/ services/
ADD models/ models/
ADD components/ components/

CMD ["python","./main.py"]
