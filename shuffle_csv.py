"""
shuffle_csv.py

Takes a csv file and shuffles the rows
"""

import pandas
import csv
import random
import numpy


usage = """
usage: python3 shuffle_csv.py <file_name>
"""


def shuffle_csv_file(file_name):
    """
    Shuffles the data in the csv file and returns it in a 
    pandas dataframe
    """
    df = pandas.read_csv(file_name)
    shuffled_list = []
    for i in range(len(df.columns)):
        lst = list(range(len(df)))
        random.shuffle(lst)
        shuffled_list.append(lst)

    shuffled_df = pandas.DataFrame([], columns=df.columns)
    for i in range(len(df)):
        lst = []
        for j in range(len(df.columns)):
            column = df.columns[j]
            lst.append(df[column][shuffled_list[j][i]])
        temp_df = pandas.DataFrame([lst], columns=df.columns)
        shuffled_df = shuffled_df.append(temp_df)

    return shuffled_df


def main(file_name):
    shuffled_data = shuffle_csv_file(file_name)
    shuffled_data.to_csv(file_name[0:-4]+'_shuffled.csv', index=False)


if __name__ == '__main__':
    import sys
    try:
        file_name = sys.argv[1]
    except:
        print(usage)
        exit(-1)
    main(file_name)
