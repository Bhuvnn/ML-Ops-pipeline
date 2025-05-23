import pandas as pd
import numpy as np
import os
import logging

from sklearn.ensemble import RandomForestClassifier
import pickle
log_dir="logs"
logger=logging.getLogger("Model Building") # Creating a logger object from logging
logger.setLevel("DEBUG") # providing the least level "DEBUG"

# Creation of Console Handler
console_handler=logging.StreamHandler() # creating a console handler to print info on console
console_handler.setLevel("DEBUG") # providing the least level "DEBUG"

log_path=os.path.join(log_dir,"model_building.log")
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
        data=df.drop(["target"],axis=1)
        label=df["target"]
        logger.debug("File loaded successfully")
        return data,label
    except FileNotFoundError as e:
        logger.error("Failed to find such file in given location %s",e)
        raise
    except Exception as e:
        logger("An unknown error detected %s",e)

def load_model(data,label):
    try:
        model=RandomForestClassifier()
        model.fit(data,label)
        logger.debug("Model loaded successfully")
        return model
    except Exception as e:
        logger.error("An unexpected error occured %s",e)
        raise

def model_score(model,data,label):
    try:
        score=model.score(data,label)
        logger.debug("Score generated successfully")
        return score
    except Exception as e:
        logger.error("An unexpected error occured")
        raise

def save_model(model,path):
    try:
        os.makedirs(path,exist_ok=True)
        file_path=os.path.join(path,"model.pkl")
        with open(file_path,"wb") as file:
            pickle.dump(model,file)
        logger.debug("Model Saved successfully")
    except Exception as e:
        logger.error("An unexpected error occured")
        raise

def main():
    train_path="data/final/final_train.csv"
    test_path="data/final/final_test.csv"
    save_path="models"
    x_train,y_train=load_data(train_path)
    x_test,y_test=load_data(test_path)
    model=load_model(x_train,y_train)
    score=model_score(model,x_test,y_test)
    save_model(model,save_path)
    print(f"model's accuracy is {score*100:.2f}%")


if __name__=="__main__":
    main()