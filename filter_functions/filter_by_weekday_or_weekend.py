__author__ = 'jacob'

"""
filter_by_weekday_or_weekend.py

Takes a dataframe and filters the values into 2 categories: weekday or weekends
"""
import pandas, numpy

weekends = [
    'Saturday',
    'Sunday',
]


def filter_data(data_frame):
    """
    Takes a data frame and filters the values into weekday or weekend
    """
    new_cols = numpy.append(data_frame.columns, 'filter')

    new_data_frame = pandas.DataFrame([], columns=new_cols)

    for i in range(len(data_frame.values)):
        value = data_frame.values[i]
        week_day = data_frame['WEEKDAY'][i]

        if week_day in weekends:
            filter_value = 'weekend'
        else:
            filter_value = 'weekday'
        
        data_frame_appender = pandas.DataFrame([numpy.append(value, filter_value)], columns=new_cols)
        new_data_frame = new_data_frame.append(data_frame_appender)

    return new_data_frame, ['weekend', 'weekday']
