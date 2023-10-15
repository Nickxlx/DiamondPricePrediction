# Code to Store pickle file (models)

import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(x_train, y_train, x_test, y_test, models):
    try:
        report = {}  # Initialize a dictionary to store the evaluation results
        for model_name, model_instance in models.items():
            # Train model
            model_instance.fit(x_train, y_train)

            # Predict Testing data
            y_test_pred = model_instance.predict(x_test)

            # Calculate the R2 score for the test data
            test_model_score = r2_score(y_test, y_test_pred)

            # Store the score in the report dictionary with the model name as the key and value as score
            report[model_name] = test_model_score

        return report  # Return the evaluation report
    
    except Exception as e:
            logging.info('Exception occured during model training')
            raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        
        raise CustomException(e,sys)