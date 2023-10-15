import sys, os
import pandas as pd
import numpy as np
from dataclasses import dataclass 
from src.logger import logging
from src.exception import CustomException

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder

#pipeline
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from src.utils import save_obj 


## Data Transformation config
@dataclass
class DataTransformationconfig:
    preprocessor_obj_fil_path = os.path.join("artifacts", "preprocessor.pkl")

# Creating Data Ingestionconfig class
class DataTranformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationconfig() 
    
    def get_data_tansformation_obj(self):
        try:
            logging.info("Data Transfromation initiated")

            # segregating catgoriacal and numarical col
            cat_cols = ['cut', 'color','clarity']
            num_cols = ['carat', 'depth','table', 'x', 'y', 'z']

            # Defining the custom ranking for ordinal encoding

            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info("Pipeline Initiated")

            # Numarical pipeline
            num_pipeline = Pipeline(steps=[
                            ("inputer", SimpleImputer(strategy="median")),
                            ("scaler", StandardScaler())
            ]
            )
            
            # Categorical pipeline
            cat_pipeline = Pipeline(steps=[
                                ("imputer", SimpleImputer(strategy="most_frequent")),
                                ("encoding", OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),
                                ("scaler", StandardScaler())
            ]
            )

            preprocessor = ColumnTransformer([
                            ("num_pipeline",num_pipeline, num_cols),
                            ("cat_pipeline", cat_pipeline, cat_cols)
            ]
            )

            return preprocessor
            logging.info("Pipeline Completed")

        except Exception as e:
            logging.info("Error in Data Trnasformation")
            raise CustomException(e,sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            # reading train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data is completed")

            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_tansformation_obj()

            ## features into independent and dependent features
            target_column_name = 'price'
            drop_columns = [target_column_name,'id']

            input_train_df = train_df.drop(drop_columns, axis = 1) 
            target_train_df = train_df[target_column_name]

            input_test_df = test_df.drop(drop_columns, axis = 1) 
            target_test_df = test_df[target_column_name]


            # apply the transformation 

            logging.info("Applying preprocessing object on training and testing datasets.")

            input_train_arr = preprocessing_obj.fit_transform(input_train_df)
            input_test_arr = preprocessing_obj.transform(input_test_df)

            # concating train and test arr with target arr
            train_arr = np.c_[input_train_arr, np.array(target_train_df)]
            test_arr = np.c_[input_test_arr, np.array(target_test_df)]

            save_obj(
                file_path = self.data_transformation_config.preprocessor_obj_fil_path, 
                obj = preprocessing_obj
            )

            logging.info("Preprocessor pickle is created and saved")

            return(
                train_arr, test_arr, 
                self.data_transformation_config.preprocessor_obj_fil_path
            )
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)
