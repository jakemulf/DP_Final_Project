"""
count_by_column.py

Takes a single csv file and a column name and generates a graph
with the counts of each value in the given column
"""

from convert_date_time import convert_csv_file
from generate_visuals import compare_file_counts
from write_data import data_frame_to_csv, get_keys


def main():
    file_name = input('Enter the csv file name: ')
    column_name = input('Enter the column name: ')

    df = convert_csv_file(file_name)
    if not column_name in df.columns:
        print('Error: the column {} is not in the file'.format(column_name))
        exit(-1)

    keys = get_keys(df, column_name)
    data_frame_to_csv(df, column_name, keys)

    compare_file_counts(['csv_files/'+str(name)+'.csv' for name in keys], [1]*len(keys))

if __name__ == '__main__':
    main()
