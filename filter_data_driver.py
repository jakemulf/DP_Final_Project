__author__ = 'jacob'

import convert_date_time, write_data
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


def main(file_name, filter_function, column):
    filter_function = get_filter_function(filter_function) 
    df = convert_date_time.convert_csv_file(file_name)

    if filter_function is None:
        if not column in df.columns:
            print('Error: The column specified does not exist in the dataframe')
            exit_with_usage(-1)
        write_data.data_frame_to_csv(df, column, None)

    else:
        filtered_df, filter_keys = filter_function(df)
        write_data.filtered_data_frame_to_csv(filtered_df, filter_keys)


def value_or_none(strn):
    if strn == 'None':
        return None
    return strn


usage = """
usage: python3 filter_data_driver.py 

valid filter functions: {filters}

If the filter function is None, you must define column to a non None value.
""".format(
    filters = list(filter_functions_dictionary.keys()),
)


def exit_with_usage(v):
    print(usage)
    exit(v)

if __name__ == '__main__':
    print(usage)
    file_name = input('Enter file name: ')
    filter_function = value_or_none(input('Enter filter function (can be None): '))
    column = input('Enter column (can be None): ')

    main(file_name, filter_function, column)
