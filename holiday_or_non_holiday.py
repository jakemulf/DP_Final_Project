"""
holiday_or_non_holiday.py

Generates descriptive statistics to compare 2 csv files, one with data
for holiday dates, and one with data for non holiday dates
"""

usage = """
usage: python3 holiday_or_non_holiday.py <file_one> <file_two>
"""

import convert_date_time


AGE_GROUPS = [
    (0,4),
    (5,9),
    (10,14),
    (15,17),
    (18,24),
    (25,34),
    (35,44),
    (45,54),
    (55,64),
    (65,74),
    (75,84),
    (85, 999),
]

def get_age_group(value):
    """
    Returns the age group of the value
    """
    for group in AGE_GROUPS:
        (_, upper_limit) = group
        if value <= upper_limit:
            return group
    return (0,0) #unreachable

def get_age_count(df):
    """
    Gets the count of the ages in the dataframe.

    If the column AGE exists, the dictionary is structured such that
    dict[age] gives the count of that specific age.

    If the column AGE_GROUP exists, the dictionary is structured such that
    dict[age_range] gives the count in that age range
    """
    count_dict = {}
    
    if 'AGE' in df.columns:
        for value in df['AGE']:
            if not value in count_dict.keys():
                count_dict[value] = 1
            else:
                count_dict[value] += 1
    
    elif 'AGE_GROUP' in df.columns:
        for value in df['AGE_GROUP']:
            group = get_age_group(value)
            if not group in count_dict.keys():
                count_dict[group] = 1
            else:
                count_dict[group] += 1

    return count_dict

def get_df_count(df):
    """
    Returns the count of the df

    If the column COUNT is defined, returns the sum of that
    column.  Else returns the length of the dataframe
    """
    if 'COUNT' in df.columns:
        return sum(df['COUNT'])
    else:
        return len(df)


def generate_statistics(df_one, df_two):
    """
    Generates comparative statistics for the 2 data frames
    """
    count_one = get_df_count(df_one)
    count_two = get_df_count(df_two)

    print('Count file one: {}, Count file two: {}'.format(count_one, count_two))

    age_group_one = get_age_count(df_one)
    age_group_two = get_age_count(df_two)

    print('Breakdown of ages for file one')
    print(age_group_one)
    print('Breakdown of ages for file two')
    print(age_group_two)


def main(file_one, file_two):
    df_one = convert_date_time.convert_csv_file(file_one)
    df_two = convert_date_time.convert_csv_file(file_two)

    generate_statistics(df_one, df_two)

if __name__ == '__main__':
    import sys
    try:
        file_one = sys.argv[1]
        file_two = sys.argv[2]
    except:
        print(usage)
        exit(-1)
    main(file_one, file_two)
