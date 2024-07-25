import os

import pandas as pd

from settings.base import DATA_DIRECTORY


class DatamartController:

    def __init__(self):
        self.data_directory = DATA_DIRECTORY
        self.dataframe = self.load_data()

    def load_data(self):
        data =[]
        if not os.path.exists(self.data_directory):
            return pd.DataFrame()

        for filename in os.listdir(self.data_directory):
            if filename.endswith('.parquet'):
                file_path = os.path.join(self.data_directory, filename)
                df = pd.read_parquet(file_path)
                data.append(df)
        return pd.concat(data, ignore_index=True)


