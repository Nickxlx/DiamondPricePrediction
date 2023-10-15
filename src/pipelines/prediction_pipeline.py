import os, sys
import pandas as pd 
from src.exception import CustomException
from src.logger import logging

from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict_for_new_data(self, features):
        try:
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl") 
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            # transforming the data for new data
            scaled_data = preprocessor.transform(features)

            pred = model.predict(scaled_data)

            return pred
        
        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    # constrocter to change the dtype of input 
    def __init__(self, carat:float,depth:float,table:float,
                x:float,y:float,z:float,
                cut:str,color:str,clarity:str):
        
        # assign the value 
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_input_data_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            
            df = pd.DataFrame(custom_input_data_dict)
            
            logging.info("DataFrame Gathered")
            return df
        except Exception as e :
            logging.info("Exception Occured in pridiction pipeline ")
            raise CustomException(e, sys)