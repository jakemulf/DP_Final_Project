__author__ = 'jacob'

"""
convert_data_time.py

Takes a csv file and converts all the date and time values to be datetime objects
"""

import pandas
import re
import datetime


def get_ints(str):
    """
    extracts all the ints from the string and removes leading 0s
    """
    int_arr = re.findall(r'\d+', str)
    for i in range(len(int_arr)):
        while int_arr[i][0] == '0' and len(int_arr[i]) > 1:
            int_arr[i] = int_arr[i][1:]
    return int_arr


def make_date(date):
    """
    Takes a date and converts it to a datetime object
    """
    date_values = list(map(int, get_ints(date)))
    return datetime.date(year=date_values[2], month=date_values[0], day=date_values[1])


def make_time(time):
    """
    Takes a time and converts it to a datetime object
    """
    time_values = list(map(int, get_ints(time)))
    return datetime.time(hour=time_values[0], minute=time_values[1])


def convert_csv_file(file_name):
    """
    Converts the given csv file to the new date_time format.
    Returns a pandas dataframe where the DATE column is datetime.date objects
    and the TIME column is datetime.time objects
    """
    data_frame =  pandas.read_csv(file_name)

    if 'DATE' in data_frame.columns:
        data_frame['DATE'] = data_frame['DATE'].apply(make_date)
    if 'TIME' in data_frame.columns:
        data_frame['TIME'] = data_frame['TIME'].apply(make_time)

    return data_frame
