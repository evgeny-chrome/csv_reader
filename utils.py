import pandas as pd


def sum_columns(file: str = '') -> dict:

    data_frame = pd.read_csv('store/' + file, sep=';')
    result = {}
    for column in data_frame.columns.values:
        number = data_frame.columns.get_loc(column)
        if number % 10 == 0 and number != 0:
            result[column] = float(data_frame[column].sum())

    return result
