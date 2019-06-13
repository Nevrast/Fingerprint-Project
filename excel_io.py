import pandas as pd
import re
def shorten_path(path):
    return re.split("/", path)[-1]

def save_to_excel(path, fp_left, fp_right):
    datasets = [fp_left, fp_right]
    sheet_names = ['left_channel', 'right_channel']
    path = shorten_path(path)
    filename = f'{path[:-4]}.xlsx'
    print(filename)
    with pd.ExcelWriter(filename) as writer:
        for data, sheet in zip(datasets, sheet_names):
            df = pd.DataFrame(data.T)
            df.to_excel(writer, sheet_name=sheet, header=None)


def load_from_excel(path):
    df_left = pd.read_excel(path, header=None, usecols='B:G', sheet_name='left_channel')
    df_right = pd.read_excel(path, header=None, usecols='B:G', sheet_name='right_channel')
    print(df_left.values.T.shape, df_right.values.T.shape)




