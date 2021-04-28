import datetime

# Secundary functions to help clean data in Class Data()

def convert_date_to_time(dict):
    '''
    if a dictionary contains a key named "Date" the functions will change
    the format from str (eg: 2021-04-03T23:38:18.584Z) to datetime.datetime for "Date" key
    :param dict: dictionary that contains a "Date" key
    :return: same input dictionary but the value of "Date" key will be in datetime.datetime format
    '''
    new_dict = dict
    for key, value in dict.items():
        if key == 'Date':
            try:
                new_value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
                new_dict[key] = new_value
            except:
                new_value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
                new_dict[key] = new_value

    return new_dict