from __future__ import print_function
import pandas as pd
import numpy as np
import glob
import os
import json
from argparse import ArgumentParser
from gooey import Gooey, GooeyParser
import openpyxl

@Gooey(program_name="Create Quarterly Marketing Report")
def parse_args():
    """ Use GooeyParser to build up the arguments we will use in our script
    Save the arguments in a default json file so that we can retrieve them
    every time we run the script.
    """
    stored_args = {}
    # get the script name without the extension & use it to build up
    # the json filename
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    args_file = "{}-args.json".format(script_name)
    # Read in the prior arguments as a dictionary
    if os.path.isfile(args_file):
        with open(args_file) as data_file:
            stored_args = json.load(data_file)
    parser = GooeyParser(description='Create Quarterly Marketing Report')
    parser.add_argument('data_directory',
                        action='store',
                        default=stored_args.get('data_directory'),
                        widget='FileChooser',
                        help="Source directory that contains Excel files")
    #print (data_file)
    args = parser.parse_args()
def combine_files(src_directory):
    """ Read in all of the sales xlsx files and combine into 1
    combined DataFrame
    """
    open_document = openpyxl.load_workbook('sample.xlsx')
    print(open_document)
        
    
if __name__ == '__main__':
    conf = parse_args()
