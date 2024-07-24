import os
import pandas as pd
from fastapi import HTTPException

from settings.base import DATA_DIRECTORY


class DatamartModel:

    def __init__(self):
        self.data_directory = DATA_DIRECTORY
        self.dataframe = self.load_data()

    def load_data(self):
        data_temporal =[]
        try:
            for filename in os.listdir(self.data_directory):
                if filename.endswith('.parquet'):
                    file_path = os.path.join(self.data_directory, filename)
                    df = pd.read_parquet(file_path)
                    data_temporal.append(df)
            return pd.concat(data_temporal, ignore_index=True)
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")

    def get_summary(self):
        try:
            return self.dataframe.describe()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating summary: {str(e)}")

    def get_data_sample(self, num_rows: int = 5):
        try:
            return self.dataframe.head(num_rows).to_dict(orient='records')
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving data sample: {str(e)}")


