__author__ = 'jacob'

import convert_date_time, write_data, column_keys
from filter_functions import filter_by_holiday, filter_by_weekday_or_weekend


filter_functions_dictionary = {
    'filter_by_holiday': filter_by_holiday.filter_data,
    'filter_by_weekday_or_weekend': filter_by_weekday_or_weekend.filter_data,
}

def get_filter_function(strn):
    """
    Takes a string and returns the filter function that maps to that string
    """
    if strn in filter_functions_dictionary.keys():
        return filter_functions_dictionary[strn]
    else:
        return None


write_data_functions_dictionary = {
    'filtered_data_frame_to_csv': write_data.filtered_data_frame_to_csv,
    'data_frame_to_csv': write_data.data_frame_to_csv,
}

def get_write_data_function(strn):
    """
    Takes a string and returns the wite data function that maps to that string
    """
    if strn in write_data_functions_dictionary.keys():
        return write_data_functions_dictionary[strn]
    else:
        return None

column_keys_dictionary = {
    'week_days': column_keys.week_days,
    'age_groups': column_keys.AGE_GROUPS,
}

def get_column_keys(strn):
    """
    Returns the column keys for the specified column
    """
    if strn in column_keys_dictionary.keys():
        return column_keys_dictionary[strn]
    else:
        return None


def main(file_name, filter_function, write_function, column_keys, column):
    filter_function = get_filter_function(filter_function)
    
    write_function = get_write_data_function(write_function)
    if write_function is None:
        print('Error: write function must be defined')
        exit(-1)
    
    column_keys = get_column_keys(column_keys)

    df = convert_date_time.convert_csv_file(file_name)

    if filter_function is None:
        if column_keys is None:
            print('Error: Having no filter function requires column keys to be specified')
            exit(-1)
        if not column in df.columns:
            print('Error: The column specified does not exist in the dataframe')
            exit(-1)
        if write_function == write_data.filtered_data_frame_to_csv:
            print('Error: Cannot call filtered_data_frame_to_csv on unfiltered data')
            exit(-1)
        write_function(df, column, column_keys)

    else:
        if write_function != write_data.filtered_data_frame_to_csv:
            print('Error: filtered data must be called with filtered_data_frame_to_csv')
            exit(-1)
        filtered_df, filter_keys = filter_function(df)
        write_function(filtered_df, filter_keys)


def value_or_none(strn):
    if strn == 'None':
        return None
    return strn


usage = """
usage: python3 filter_data_driver.py <file_name> <filter_function>* <write_function> <column_keys>* <column>*

*: Can use the keyword 'None' to specify no value

valid filter functions: {filters}
valid write functions: {writes}
valid column keys: {column_keys}

If the filter function is None, you must define column_keys and column to non None values.
In addition, the write function must be data_frame_to_csv.
""".format(
    filters = list(filter_functions_dictionary.keys()),
    writes = list(write_data_functions_dictionary.keys()),
    column_keys = list(column_keys_dictionary.keys())
)

if __name__ == '__main__':
    import sys
    try:
        file_name = sys.argv[1]
        filter_function = value_or_none(sys.argv[2])
        write_function = sys.argv[3]
        column_keys = value_or_none(sys.argv[4])
        column = sys.argv[5]
    except:
        print(usage)
        exit(-1)
    main(file_name, filter_function, write_function, column_keys, column)
