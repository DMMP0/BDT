# docker build -t bdt/source-layer .

# docker run -d --name 0-Source-Layer-BDT --network app-tier bdt/source-layer

FROM python:latest
LABEL Mantainer1="huma.rehman@studenti.unitn.it", Mantainer2="maurizio.demarchi@studenti.unitn.it", Mantainer3="stefano.moro@studenti.unitn.it"

# set working directory,
WORKDIR /user/app/scr/BDT/Source

# install libraries
RUN pip install pandas
RUN pip install uuid
RUN pip install numpy
RUN pip install python-docx
RUN pip install ccard
RUN pip install openpyxl
RUN pip install redis

ADD main.py .
ADD data_generation.py .
ADD 0.Client_List.csv .
ADD company_information.csv .

ADD services/ services/
ADD models/ models/
ADD components/ components/
ADD assets/ assets/

CMD ["stdbuf", "-oL","python", "data_generation.py"]
CMD ["stdbuf", "-oL","python","main.py"] 

## main.py sends the data to redis

