__author__ = 'jacob'

"""
generate_visuals.py

Takes a list of csv files and creates visuals for them
"""

import matplotlib.pyplot as plt

from convert_date_time import convert_csv_file


def plot_incident_bar_graphs(csv_files):
    """
    Takes csv files and creates bar graphs showing the incidents for each category in
    the csv files

    Currently makes a scatter plot
    """
    count_list = []
    for file in csv_files:
        data_frame = convert_csv_file(file)
        count = 0
        for curr_count in data_frame['COUNT'].values:
            count += curr_count
        count_list.append(count)
    
    plt.scatter(list(range(len(count_list))), count_list)
    plt.show()
