__author__ = 'jacob'

"""
filter_by_holiday.py

Takes a dataframe with converted dates and times, and filters the dataframe
into categories based on the holidays
"""
import pandas, numpy

def labor_day(date):
    return date.month == 9 and (date.weekday() in [0,5,6]) and date.day < 7


def forth_of_july(date):
    return date.month == 7 and date.day == 4

holiday_functions = [
    labor_day,
    forth_of_july,
]

# holiday_functions[i] and holiday_names[i] must map to the same holiday

holiday_names = [
    'Labor Day',
    'Forth of July',
    'No Holiday',
]


def filter_data(data_frame):
    """
    Takes a data frame created by convert_date_time.convert_csv_file and returns
    a dictionary filtered by the given holidays
    """
    new_cols = numpy.append(data_frame.columns, 'filter')

    new_data_frame = pandas.DataFrame([], columns=new_cols)

    for i in range(len(data_frame.values)):
        value = data_frame.values[i]
        date = data_frame['DATE'][i]

        holiday_index = -1

        for j in range(len(holiday_functions)):
            func = holiday_functions[j]
            if func(date):
                holiday_index = j                
                break
        data_frame_appender = pandas.DataFrame([numpy.append(value, holiday_names[holiday_index])], columns=new_cols)
        new_data_frame = new_data_frame.append(data_frame_appender)

    return new_data_frame, holiday_names
