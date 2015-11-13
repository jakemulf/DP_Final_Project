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
    for file in csv_files:
        data_frame = convert_csv_file(file)
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
    plt.show()

