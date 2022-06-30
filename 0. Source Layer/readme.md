# Source Layer

The aim of this layer is to generate and parse the data, sending it to Redis (the persistence layer).

***NB: this layer was designed with Python 3.10 in mind.***

***NB: an instance of redis-server must run in order for this layer to work.*** In order to do that [Redis](https://redis.io/download/) must be downloaded.
Once downloaded and installed, an instance of Redis server can simply be started by typing *redis-server* in your terminal.
If you want to check what's going under the hood, you can get all the keys with the command _'keys \*_'. If you already have other keys in your redis instance, a better
option would be _'keys \*(\*).\*'_. If you want to see the content of a specific key, the command _'get "**Key name**"'_ shold be issued. For multiple keys, the command _mget_
can be used. 

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
   - inscred;
   - investigation;
   - accused;
   - condemned;
   - civ pass

You can expect the script to generate ~ 197 reports every ~7 seconds (for a total of 3.2 MB).

The script will come in the following file formats:
- txt
- html
- xlsx
- docx
- csv

## Sending data to Redis

The data can be sent to redis by simply starting the main.py script.

The script will continuously send all the files to redis (deleting them from the "reports" folder), waiting 10s after doing so.
The files can be found as redis strings, having the filename as key *(e.g. 'Oberbank AG(Questura).xlsx')*.
The script is multithreaded and will start a thread for every file format.
