from __future__ import print_function
import pandas as pd
import numpy as np
import glob
import csv
import codecs
import os
import json
from argparse import ArgumentParser
from gooey import Gooey, GooeyParser
import time

from openpyxl import load_workbook
import sys

@Gooey(program_name="DIgiKey Format Picking Tool")
def parse_args():
    # Read in the prior arguments as a dictionary
    parser = GooeyParser(description='Crosspoint Technologies LLP')
    edit_data = parser.add_argument('sourcd_directory',
                        action='store',
                        widget='FileChooser',
                        help="Source directory that contains Excel files")
    args = parser.parse_args()
    return args
if __name__ == '__main__':
    conf = parse_args()
    edit = str(conf)
    location = edit.split("'",1)[1]
    final = location[:-2]
    #print(final)
    #final1= ""
    #final1 = str(final)
    #print (final1)
    #open_document =load_workbook(final)
    #print(open_document)
    #sheet = open_document.get_sheet_by_name('abc')
    #print(sheet['B2'].value)
    #open_document.save('sample_updated.xlsx')
    df = pd.read_csv(final)
    #df.rename(columns={df.columns[0]: 'Cost' }, inplace=True)
    # select desired columns
    print ('Document Opened')
    time.sleep(2)
    df = df[['Description', 'DigiKey Part #', 'MFG Part Number', 'Quantity']]
    time.sleep(2)
    print ('Filtering the particular data to seperate document')
    #write to the file (tab separated)
    df.to_csv('output_data.csv', index=False)
    time.sleep(4)
    print ('The Selected datas are copied successfully into the file name "output_data.csv"')
    time.sleep(2)
    print ('Find the file at the Document folder')
