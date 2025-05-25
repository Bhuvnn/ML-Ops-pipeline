import pandas as pd
import os
import logging
from sklearn.model_selection import train_test_split
import yaml
log_dir="logs"
os.makedirs(log_dir,exist_ok=True)




# Creation of Logger
logger=logging.getLogger("data_ingestion") # Creating a logger object from logging
logger.setLevel("DEBUG") # providing the least level "DEBUG"

# Creation of Console Handler
console_handler=logging.StreamHandler() # creating a console handler to print info on console
console_handler.setLevel("DEBUG") # providing the least level "DEBUG"

log_path=os.path.join(log_dir,"data_ingestion.log")
file_handler=logging.FileHandler(log_path) # Creating a file handler to save same info in a log file
file_handler.setLevel("DEBUG") # setting the level to "DEBUG"

formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") # Creating and Setting the format of saving and displaying the info
console_handler.setFormatter(formatter) # Adding the formatter in console handler
file_handler.setFormatter(formatter) # Adding the formatter to file handler

logger.addHandler(console_handler) # passing the handler back to logger
logger.addHandler(file_handler) # passing the handler back to logger

def load_params(path):
    with open(path,"r") as f:
        params=yaml.safe_load(f)
    return params

def load_data (data_url):
    try:
        df=pd.read_csv(data_url,encoding='latin-1')
        logger.debug(f"Data loaded from {data_url} ")
        return df
    except pd.errors.ParserError as e:
        print("Failed to parse the csv file %s", e)
        raise
    except Exception as e:
        print("Unexpecter error has occured %s", e) 
        raise
    
    

def preprocess_data(df):
    try:
        df.drop(["Unnamed: 2","Unnamed: 3","Unnamed: 4"],axis=1,inplace=True)
        df.rename(columns={"v1":"target","v2":"text"},inplace=True)
        logger.debug("Preprocessing completed")
        return df
    except KeyError as e:
        logger.error("Missing columns is dataframe %s",e)
        raise
    except Exception as e:
        logger.error("An unexpected error has occured %s",e)
        raise

def save_data(train_data,test_data,data_path):
    try: 
        os.makedirs(data_path,exist_ok=True)
        train_data.to_csv(os.path.join(data_path,"train.csv"),index=False)
        test_data.to_csv(os.path.join(data_path,"test.csv"),index=False)
        logger.debug("test dataframe and train dataframe is created")
    except Exception as e:
        logger.error("Falsed to save the data %s",e)
        raise

def main():
    path="Experiments\spam.csv"
    yaml_path="params.yaml"
    try:
        params=load_params(yaml_path)
        test_size=params["data_ingestion"]["test_size"]
        df=load_data(path)
        new_df=preprocess_data(df)
        train_data,test_data=train_test_split(new_df,test_size=test_size,random_state=3)
        save_data(train_data=train_data,test_data=test_data,data_path="data")
        logger.debug("Data is saved")
    except Exception as e:
        logger.error("Failed to save data %s",e)
        raise 
        

if __name__=="__main__":
    main()      
    

