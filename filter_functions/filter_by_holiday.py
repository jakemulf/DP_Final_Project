__author__ = 'jacob'

"""
filter_by_holiday.py

Takes a dataframe with converted dates and times, and filters the dataframe
into categories based on the holidays
"""


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
    data_frame_dict = {}
    for name in holiday_names:
        data_frame_dict[name] = []

    for i in range(len(data_frame.values)):
        value = data_frame.values[i]
        date = data_frame['DATE'][i]

        is_holiday = False

        for j in range(len(holiday_functions)):
            func = holiday_functions[j]
            if func(date):
                is_holiday = True
                data_frame_dict[holiday_names[j]].append(value)
                break

        if not is_holiday:
            data_frame_dict[holiday_names[-1]].append(value)

    return data_frame_dict
