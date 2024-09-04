import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Note 1: Build csv_path as "absolute path" in order to call this method from anywhere.
        # Note 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        parent = os.path.dirname(os.path.dirname(__file__))
        csv_path = os.path.join(parent,'data','csv')
        files_names = os.listdir(csv_path)
        files_names = [file for file in files_names if file.endswith('.csv')]
        keys_names = [file.replace('.csv','').replace('olist_','').replace('_dataset','') for file in files_names]
        dict_files_names = [(x,pd.read_csv(os.path.join(csv_path, y))) for x, y in zip(keys_names, files_names)]
        dict_files_names = dict(dict_files_names)

        return dict_files_names

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
