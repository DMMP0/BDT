# Source Layer

The aim of this layer is to generate and parse the data, sending it to Redis (the persistence layer).

***NB: this layer was designed with Python 3.10 in mind.***

***NB: an instance of a redis container must run in order for this layer to work.*** 
It can be instantiated with the following command: *docker run -d --name redis --network app-tier redis*

## Data generation 

In order to start the data generation the 'data_generation.py' script must run.
For each company, the script will generate the following files:
1. A Declaration file, with the following information of each founder member:
   - Fiscal code (Id_Number);
   - first name;
   - last name;
   - sex;
   - Date of birth (DOB);
   - ethnicity;
   - education;
   - phone number;
   - Personal email;
   - purpose for the asked loan;
   - registration number of the company;
   - company name;
   - established date;
   - country;
   - number of employees;
   - email;
   - amount of credit;
   - duration in months;
2. A Bank file, with the following additional information:
   - bank  name;
   - bank  country;
   - open  new  credit  in  6  months;
   - amount  in  6  months;
   - new  credit  in  12  months;
   - new  credit  in  18  months;
   - amount  in  12  months;
   - amount  in  18  months;
   - house  mortgage;
   - amount  of  house  mortgage;
   - amount  due  mortgage;
   - house  property;
   - total  house  amount;
   - credit  card  number;
   - credit  card  limit  total;
   - actual  debit  credit  cards;
   - monthly  income;
   - savings;
   - other  savings;
3. A Broker file, with the following additional information:
   - Broker agency country;
   - Broker agency name;
   - from 30 to 60;
   - from 60 to 90;
   - more than 90;
   - debit id;
   - insolvent;
   - insolvent amount
4. A Questura (police department for criminal records) file, with the following additional information:
   - questura country;
   - if bankruptcy was declared;
   - whether it was fraudolent
   - insolvency credit;
   - investigation;
   - accused;
   - condemned;
   - passive actor in civil trial

You can expect the script to generate ~ 197 reports every ~7 seconds (for a total of 3.2 MB).

The script will come in the following file formats:
- txt
- html
- xlsx
- docx
- csv

## Sending data to Redis container

The program can be started by:
1. building the image: *docker build -t bdt/source-layer .*
2. starting the container: *docker run -d --name 0-Source-Layer-BDT --network app-tier bdt/source-layer*
