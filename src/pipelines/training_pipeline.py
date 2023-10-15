import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException

from src.components.data_ingention import DataIngestion

from src.components.data_transformation import DataTranformation

from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    # data ingesetion initialization
    ingesetion_obj = DataIngestion()
    train_data_path, test_data_path= ingesetion_obj.initiat_data_ingestion()
    
    print(train_data_path,test_data_path)

    # data transformation initialization
    transformation_obj = DataTranformation()
    train_arr, test_arr,_ = transformation_obj.initiate_data_transformation(train_data_path, test_data_path)

    # model training initialization 
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_arr, test_arr)