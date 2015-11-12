__author__ = 'jacob'

"""
write_data.py

Writes a pandas dataframe to multiple csv files.
Can use filtered data, or can specify what values in the
dataframe to use
"""

import csv


def write_to_csv(file_name, values):
    """
    writes the values to a csv file with the given file name
    """
    with open('csv_files/'+file_name+'.csv', 'w+') as f:
        csv_writer = csv.writer(f)
        for value in values:
            csv_writer.writerow(value)


def filtered_data_frame_to_csv(filtered_data_frame, filter_keys):
    """
    Creates multiple csv files where each csv file has the name of a value in the
    given filter keys and contains all the values with that filter value
    """
    for key in filter_keys:
        values = filtered_data_frame[filtered_data_frame['filter'] == key]
        write_to_csv(key, values.values)

def data_frame_to_csv(data_frame, column, keys):
    """
    Creates multiple csv files where each csv file has the name of a value
    in the given keys in the given column and contains rows in the
    dataframe that match that key.
    """
    for key in keys:
        values = data_frame[data_frame[column] == key]
        write_to_csv(key, values.values)
