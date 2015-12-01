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
            curr_count = len(df)
        else:
            curr_count = sum([x for x in df['COUNT'] if not math.isnan(x)]) \
                        * count_normalizations[i]

        if curr_count > max_count:
            max_count = curr_count
        plt.scatter(i, curr_count, c=rand_color())

    plt.xlim(-.5, len(file_list)-.5)
    plt.ylim(0, max_count*1.5)
    plt.legend(file_list, loc='upper left')
    plt.show()


def main():
    file_list = []
    while True:
        curr_file = input('Enter file name (enter None to finish): ')
        if curr_file == 'None':
            break
        file_list.append(curr_file)

    count_normalizations = []
    for i in range(len(file_list)):
        numerator = int(input('Enter numerator for file {}: '.format(file_list[i])))
        denominator = int(input('Enter denominator for file {}: '.format(file_list[i])))
        count_normalizations.append(numerator/denominator)

    compare_file_counts(file_list, count_normalizations)

if __name__ == '__main__':
    main()
