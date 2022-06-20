import os
import pandas as pd
import html_to_json
import docx
import io
import csv
from docx import Document
import mdtex2html


path = 'reports'
excel = [f for f in os.listdir(path) if f.endswith('.xlsx')]
html = [f for f in os.listdir(path) if f.endswith('.html')]
tex = [f for f in os.listdir(path) if f.endswith('.tex')]
word = [f for f in os.listdir(path) if f.endswith('.docx')]
txt = [f for f in os.listdir(path) if f.endswith('.txt')]



def read_docx_tables(filename, tab_id=None, **kwargs):
    """
    parse table(s) from a Word Document (.docx) into Pandas DataFrame(s)

    Parameters:
        filename:   file name of a Word Document

        tab_id:     parse a single table with the index: [tab_id] (counting from 0).
                    When [None] - return a list of DataFrames (parse all tables)

        kwargs:     arguments to pass to `pd.read_csv()` function

    Return: a single DataFrame if tab_id != None or a list of DataFrames otherwise
    """
    def read_docx_tab(tab, **kwargs):
        vf = io.StringIO()
        writer = csv.writer(vf)
        for row in tab.rows:
            writer.writerow(cell.text for cell in row.cells)
        vf.seek(0)
        return pd.read_csv(vf, **kwargs)

    doc = Document(filename)
    if tab_id is None:
        for tab in doc.tables:
            df = read_docx_tab(tab, **kwargs) 
        return df
    else:
        try:
            return read_docx_tab(doc.tables[tab_id], **kwargs)
        except IndexError:
            print('Error: specified [tab_id]: {}  does not exist.'.format(tab_id))
            raise
print(len(excel))

# columns=['registeration_number','name','establied_date','country','number_of_employes','purpose','phone_number','email','bank_name','bank_country']
###read excel
for i in range(0,len(excel)):
    # Read a text file to a dataframe using read_table function

    data =  pd.read_excel('reports/' + str(excel[i]))
    data = pd.DataFrame(data)
    columns = data.columns
    name = str(excel[i]).split('.')[0]
    temp = data.to_json('./jsons/'+name+ '.json',indent=4,orient='index')

for i in range(0,len(html)):
    # Read a text file to a dataframe using read_table function
    name = str(html[i]).split('.')[0]
    data =  pd.read_html('reports/' + str(html[i]))
    data[0].to_json('./jsons/'+name+ '.json',indent=4,orient='index')

for i in range(0,len(word)):
    
# Load the first table from your document. In your example file,
# there is only one table, so I just grab the first one.
    document = Document('reports/' + str(word[i]))
    table = document.tables[0]

    # Data will be a list of rows represented as dictionaries
    # containing each row's data.
    data = []

    keys = None
    for i, row in enumerate(table.rows):
        name = str(word[i]).split('.')[0]
        df = read_docx_tables('reports/' + str(word[i]))
        df = pd.DataFrame(df)
        df = pd.DataFrame(df.values,columns=columns[1:])
        df.to_json('./jsons/'+name+ '.json',indent=4,orient='index')


for i in range(0,len(txt)):
    # Read a text file to a dataframe using read_table function
    name = str(txt[i]).split('.')[0]
    data =  pd.read_csv('reports/' + str(txt[i]), sep='\t')
    data = pd.DataFrame(data)
    temp = data.to_json('./jsons/'+name+ '.json',indent=4,orient='index')





