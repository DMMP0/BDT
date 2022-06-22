

FROM python:latest
LABEL Mantainer1="huma.rehman@studenti.unitn.it", Mantainer2="maurizio.demarchi@studenti.unitn.it", Mantainer3="stefano.moro@studenti.unitn.it"

# set working directory,
WORKDIR /user/app/scr

# install libraries
RUN pip install pandas
RUN pip install uuid
RUN pip install numpy
RUN pip install python-docx
RUN pip install ccard

RUN pip install redis

ADD main.py .
ADD data_generation.py .
ADD services/ services/
ADD models/ models/
ADD components/ components/

CMD ["python", "data_generation.py"]
CMD ["python","./main.py"]

