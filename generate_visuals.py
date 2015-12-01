__author__ = 'jacob'

"""
generate_visuals.py

Takes a list of csv files and creates visuals for them
"""

import matplotlib.pyplot as plt
import pandas
import math
import random

from convert_date_time import convert_csv_file


def rand_color():
    """
    Makes a random RGB color
    """
    return (random.random(), random.random(), random.random())

def compare_file_counts(file_list, count_normalizations):
    """
    Creates a plot that compares the counts of each file

    Normalizes the data to give a rate per day
    """
    max_count = 0
    for i in range(len(file_list)):
        file_name = file_list[i]
        df = pandas.read_csv(file_name)
        if not 'COUNT' in df.columns:
            print('COUNT must be in the dataframe')
            exit(-1)
        
        curr_count = sum([x for x in df['COUNT'] if not math.isnan(x)]) \
                        * count_normalizations[i]
        if curr_count > max_count:
            max_count = curr_count
        plt.scatter(i, curr_count, c=rand_color())

    plt.xlim(-.5, len(file_list)-.5)
    plt.ylim(0, max_count*1.5)
    plt.legend(file_list)
    plt.show()
