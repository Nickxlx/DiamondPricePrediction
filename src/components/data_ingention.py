import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# initializing the data ingestion configuration

@dataclass
class DataIngestionconfig:
    raw_data_path = os.path.join("artifacts", "raw.csv")
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")


# create a data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiat_data_ingestion(self):
        logging.info("Data Ingetion method starts")

        try:
            # reading the dataset
            df = pd.read_csv(os.path.join("notebooks/data", "gemstone.csv"))
            logging.info("Data Read as pandas DataFrame")

            # creating dir for storing the raw data
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # storing the raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            logging.info("Train Test split")
            train_set, test_set = train_test_split(df, test_size=0.30, 
                                                random_state=42)

            # storing train and test data 
            train_set.to_csv(self.ingestion_config.train_data_path,             
                            index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)

            logging.info("Data Ingetion is completed")

            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path)

        except Exception as e:
            logging.info("Error occured in Data Ingestion config")
