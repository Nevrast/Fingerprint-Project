import pandas as pd
import os


def save_to_excel(path, fp_left, fp_right, time_bins):
    datasets = [fp_left, fp_right, time_bins]
    sheet_names = ['left_channel', 'right_channel', 'time_bins']
    _, file = os.path.split(path)
    filename = f'{file[:-4]}.xlsx'
    print(filename)
    with pd.ExcelWriter(filename) as writer:
        for data, sheet in zip(datasets, sheet_names):
            df = pd.DataFrame(data.T)
            df.to_excel(writer, sheet_name=sheet, header=None)


def load_from_excel(path):
    df_left = pd.read_excel(path, header=None, usecols='B:G', sheet_name='left_channel')
    df_right = pd.read_excel(path, header=None, usecols='B:G', sheet_name='right_channel')
    df_time = pd.read_excel(path, header=None, usecols='B', sheet_name='time_bins')
    return df_left.values.T, df_right.values.T, df_time




