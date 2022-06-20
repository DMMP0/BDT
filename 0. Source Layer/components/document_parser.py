import os
import pandas as pd
# import html_to_json
# import docx  -- must install python-docx and openpyxl
import io
import csv
from docx import Document

# import mdtex2html


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


# print(len(excel))

columns = ['registeration_number', 'name', 'establied_date', 'country', 'number_of_employes', 'purpose', 'phone_number',
           'email', 'bank_name', 'bank_country']


# read excel
def excel_to_dict(filepath: str) -> dict:
    """The function returns a dictionary from a filepath. The dictionary will have the filename as key and the values
    as another dictionary"""
    global columns

    # Read a text file to a dataframe using read_table function

    data = pd.read_excel(filepath)
    data = pd.DataFrame(data)
    columns = data.columns
    name = str(filepath).split('/')[-1]
    return {name: data.to_dict(orient='index')}
    # temp = data.to_json('./jsons/' + name + '.json', indent=4, orient='index')


def html_to_dict(filepath: str) -> dict:
    """The function returns a dictionary from a filepath. The dictionary will have the filename as key and the values
        as another dictionary"""
    # Read a text file to a dataframe using read_table function
    name = filepath.split('/')[-1]
    data = pd.read_html(filepath)
    return {name: data[0].to_dict(orient='index')}
    # data[0].to_json('./jsons/' + name + '.json', indent=4, orient='index')


def docx_to_dict(filepath: str) -> dict:
    """The function returns a dictionary from a filepath. The dictionary will have the filename as key and the values
        as another dictionary"""
    global columns
    name = filepath.split('/')[0]
    df = read_docx_tables(filepath)
    df = pd.DataFrame(df)
    df = pd.DataFrame(df.values,
                      columns=['registeration_number', 'name', 'establied_date', 'country', 'number_of_employes',
                                   'purpose', 'phone_number', 'email', 'bank_name', 'bank_country'])  # NB: don't modify
    return {name: df.to_dict(orient='index')}
    # df.to_json('./jsons/' + name + '.json', indent=4, orient='index')


def txt_to_dict(filepath: str) -> dict:
    """The function returns a dictionary from a filepath. The dictionary will have the filename as key and the values
           as another dictionary"""
    # Read a text file to a dataframe using read_table function
    name = str(filepath).split('/')[0]
    data = pd.read_csv(filepath, sep='\t')
    data = pd.DataFrame(data)
    return {name:data.to_dict(orient='index')}
    # temp = data.to_json('./jsons/' + name + '.json', indent=4, orient='index')
