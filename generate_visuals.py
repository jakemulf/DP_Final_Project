__author__ = 'jacob'

"""
generate_visuals.py

Takes a list of csv files and creates visuals for them
"""

import matplotlib.pyplot as plt

from convert_date_time import convert_csv_file


def plot_incident_bar_graphs(csv_files):
    """
    Takes csv files and creates a scatter plot showing the incidents for each category in
    the csv files
    """
    count_list = []
    max_count = 0
    for file_name in csv_files:
        data_frame = convert_csv_file(file_name)
        if not 'COUNT' in data_frame.columns:
            print('Error: the csv file must have a COUNT column')
            exit(-1)
        count = 0
        for curr_count in data_frame['COUNT'].values:
            count += curr_count
        count_list.append(count)
        if count > max_count:
            max_count = count

    plt.ylim(0,max_count*1.5)
    plt.xlim(-.5,len(count_list)-.5)
    plt.scatter(list(range(len(count_list))), count_list)
    plt.legend(csv_files)
    plt.show()


def plot_count_by_column(file_name, column_name):
    """
    Plots the data in the csv file to compare by a specific column
    """
    data_frame = convert_csv_file(file_name)
    if not column_name in data_frame.columns:
        print('Error: the given column name is not in the file')
        exit(-1)

    frequency_dict = {}
    column_index = data_frame.columns.get_loc(column_name)
    count_index = -1
    if 'COUNT' in data_frame.columns:
        count_index = data_frame.columns.get_loc('COUNT')

    for value in data_frame.values:
        addend = 1
        if count_index >= 0:
            addend = value[count_index]

        if value[column_index] in frequency_dict.keys():
            frequency_dict[value[column_index]] += addend

        else:
            frequency_dict[value[column_index]] = addend

    dict_keys = list(frequency_dict.keys())

    for i in range(len(dict_keys)):
        key = dict_keys[i]
        plt.scatter(i, frequency_dict[key])

    plt.legend(dict_keys)
    plt.show()
