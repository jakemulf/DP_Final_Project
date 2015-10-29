__author__ = 'jacob'

"""
convert_data_time.py

Takes a csv file and converts all the date and time values to be in a form that's
easy to use for the python datetime module.  For example, a date like 5/1/2007
will be rewritten as 5 1 2007
"""

import pandas
import re


def get_ints(str):
    """
    extracts all the ints from the string and removes leading 0s
    """
    int_arr = re.findall(r'\d+', str)
    for i in range(len(int_arr)):
        while int_arr[i][0] == '0' and len(int_arr[i]) > 1:
            int_arr[i] = int_arr[i][1:]
    return int_arr


def convert_csv_file(file_name):
    """
    Converts the given csv file to the new date_time format.
    Rewrites the new file as file_name_conversion.csv
    """
    data_frame =  pandas.read_csv(file_name)
    for i in range(len(data_frame['DATE'])):
        date_values = list(map(int, get_ints(data_frame['DATE'][i])))
        data_frame['DATE'][i] = date_values
    for i in range(len(data_frame['TIME'])):
        time_values = list(map(int, get_ints(data_frame['TIME'][i])))
        data_frame['TIME'][i] = time_values

    data_frame.to_csv(file_name[:-4]+'_conversion.csv', index=False)