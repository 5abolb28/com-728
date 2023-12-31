#Load Function

import pandas as pd
'''
Python Function to load data csv file from path into a dataframe
'''
def load_data_from_path(df_path):
    df = pd.read_csv(df_path)
    return df

