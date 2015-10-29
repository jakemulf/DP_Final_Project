__author__ = 'jacob'

"""
filter_by_day_of_week.py

Takes a csv file and filters the values by the day of the week
"""

import pandas

days = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
]

def filter_data(data_frame):
    """
    Takes a data frame and returns 7 new data frams, 1 for each
    day of the week
    """
    data_frame_dict = {}
    for day in days:
        data_frame_dict[day] = []

    for i in range(len(data_frame.values)):
        value = data_frame.values[i]
        week_day = data_frame['WEEKDAY'][i]
        data_frame_dict[week_day].append(value)

    return data_frame_dict

print(filter_data(pandas.read_csv('DummyData_DayofTheWeek.csv')))