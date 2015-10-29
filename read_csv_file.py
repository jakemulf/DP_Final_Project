__author__ = 'jacob'

import datetime
import csv
import re


def get_ints(str):
    """
    extracts all the ints from the string
    """
    int_arr = re.findall(r'\d+', str)
    for i in range(len(int_arr)):
        if int_arr[i][0] == '0' and len(int_arr[i]) > 1:
            int_arr[i] = int_arr[i][1:]
    return int_arr


def get_dates(date_time_arr):
    """
    Takes a date_time array such that date_time_arr[i] == [some date, some time]

    Returns an array of dates and an array of times using the datetime module
    """
    dates = []
    times = []
    for date_time in date_time_arr:
        curr_date = list(map(int, get_ints(date_time[0])))
        curr_time = list(map(int, get_ints(date_time[1])))
        print(curr_date)
        print(curr_time)
        dates.append(datetime.date(year=curr_date[2], month=curr_date[0], day=curr_date[1]))
        times.append(datetime.time(hour=curr_time[0], minute=curr_time[1]))

    return dates, times


file = csv.reader(open('Dummy.csv'))
arr = []

for line in file:
    arr.append(line)

dates, times = get_dates(arr[1:])
dates = list(filter(lambda x: x > datetime.date(2007, 5, 27) and x < datetime.date(2007, 5, 29), dates))

print(dates)