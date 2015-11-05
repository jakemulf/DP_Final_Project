__author__ = 'jacob'

"""
data_frame_dict_to_csv.py

Takes a data frame dictionary generated by one of the filtering functions
and writes it to a csv file
"""

import csv


def write_to_csv(file_name, values):
    """
    writes the values to a csv file with the given file name
    """
    with open(file_name+'.csv', 'w+') as f:
        csv_writer = csv.writer(f)
        for value in values:
            csv_writer.writerow(value)


def dict_to_csv(data_frame_dict):
    """
    Creates multiple csv files where each csv file has the name of a key in the
    dictionary and the values corresponding to that key
    """
    for key in data_frame_dict.keys():
        write_to_csv(key, data_frame_dict[key])