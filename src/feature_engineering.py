import pandas as pd
import numpy as np
import os
import logging

from data_ingestion import load_params
from sklearn.feature_extraction.text import TfidfVectorizer
log_dir="logs"
logger=logging.getLogger("Feature Engineering") # Creating a logger object from logging
logger.setLevel("DEBUG") # providing the least level "DEBUG"

# Creation of Console Handler
console_handler=logging.StreamHandler() # creating a console handler to print info on console
console_handler.setLevel("DEBUG") # providing the least level "DEBUG"

log_path=os.path.join(log_dir,"feature_engineering.log")
file_handler=logging.FileHandler(log_path) # Creating a file handler to save same info in a log file
file_handler.setLevel("DEBUG") # setting the level to "DEBUG"

formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") # Creating and Setting the format of saving and displaying the info
console_handler.setFormatter(formatter) # Adding the formatter in console handler
file_handler.setFormatter(formatter) # Adding the formatter to file handler

logger.addHandler(console_handler) # passing the handler back to logger
logger.addHandler(file_handler) # passing the handler back to logger

def load_data(path):
    try:
        df=pd.read_csv(path)
        logger.debug("Data Loading completed")
        return df
    except FileNotFoundError as e:
        logger.error("file not found %s",e)

def features(train_df,test_df,max_features):
    try:
        
        train_df = train_df.dropna(subset=['text'])
        test_df = test_df.dropna(subset=['text'])
        
        x_train=train_df["text"]
        x_test=test_df["text"]
        
        vector=TfidfVectorizer(max_features=max_features)
        x_train=vector.fit_transform(x_train).toarray()
        x_test=vector.transform(x_test).toarray()
        x_train_df = pd.DataFrame(x_train, index=train_df.index)
        x_test_df = pd.DataFrame(x_test, index=test_df.index)

        train_df = pd.concat([train_df.drop(columns=["text"]), x_train_df], axis=1)
        test_df = pd.concat([test_df.drop(columns=["text"]), x_test_df], axis=1)
        logger.debug("features are extracted and applied on dataframe")
        return train_df,test_df
    
    except Exception as e:
        logger.error("Error during execution %s",e)
        raise

def save_data(train_data,test_data):
    path=os.path.join("data","final")
    os.makedirs(path,exist_ok=True)
    
    train_data.to_csv(os.path.join(path,"final_train.csv"),index=False)
    test_data.to_csv(os.path.join(path,"final_test.csv"),index=False)
    logger.debug("files are saved successfully")        
    

def main():
    yaml_path="params.yaml"
    params=load_params(yaml_path)
    max_features=params["feature_engineering"]["max_features"]
    train_path="data\intermin\preprocessed_train.csv"
    test_path="data\intermin\preprocessed_test.csv"
    train_df=load_data(train_path)
    test_df=load_data(test_path)
    
    train_data,test_data=features(train_df,test_df,max_features)
    save_data(train_data,test_data)


if __name__=="__main__":
    main()