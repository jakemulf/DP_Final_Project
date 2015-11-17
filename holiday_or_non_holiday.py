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
    column.  Otherwise, returns the length of the dataframe
    since each row in the dataframe will be a single incident
    """
    if 'COUNT' in df.columns:
        return sum(df['COUNT'])
    else:
        return len(df)


def get_average_age(df):
    """
    Returns the average age of the dataframe

    Returns -1 if there is no AGE column
    """
    if 'AGE' in df.columns:
        return sum(df['AGE'])/len(df)
    else:
        return -1


def get_gender_count(df):
    """
    Returns a dictionary with 2 keys (M,F) where
    each key gives the count of that gender

    Returns an empty dictionary if the GENDER
    column does not exist
    """
    gender_counts = {}

    if 'GENDER' in df.columns:
        gender_counts['M'] = 0
        gender_counts['F'] = 0

        for value in df['GENDER']:
            gender_counts[value] += 1

    return gender_counts


def generate_statistics(df_one, df_two):
    """
    Generates comparative statistics for the 2 data frames
    """
    count_one = get_df_count(df_one)
    count_two = get_df_count(df_two)

    print('Count file one: {}, Count file two: {}'.format(count_one, count_two))

    gender_count_one = get_gender_count(df_one)
    gender_count_two = get_gender_count(df_two)

    print('Gender breakdown for file one')
    print(gender_count_one)
    print('Gender breakdown for file two')
    print(gender_count_two)

    age_group_one = get_age_count(df_one)
    age_group_two = get_age_count(df_two)

    print('Breakdown of ages for file one')
    print(age_group_one)
    print('Breakdown of ages for file two')
    print(age_group_two)

    average_age_one = get_average_age(df_one)
    average_age_two = get_average_age(df_two)

    print('Average age file one: {}, Average age file two: {}'.format(average_age_one, average_age_two))


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
