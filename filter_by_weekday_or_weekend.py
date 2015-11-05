__author__ = 'jacob'

"""
filter_by_weekday_or_weekend.py

Takes a dataframe and filters the values into 2 categories: weekday or weekends
"""

weekends = [
    'Saturday',
    'Sunday',
]


def filter_data(data_frame):
    """
    Takes a data frame and filters the values into weekday or weekend
    """
    weekday = 'weekday'
    weekend = 'weekend'

    data_frame_dict = {}
    data_frame_dict[weekday] = []
    data_frame_dict[weekend] = []

    for i in range(len(data_frame.values)):
        value = data_frame.values[i]
        week_day = data_frame['WEEKDAY'][i]

        if week_day in weekends:
            data_frame_dict[weekend].append(value)
        else:
            data_frame_dict[weekday].append(value)

    return data_frame_dict