import logging
import os
import pickle

from model_building import load_data

dir="logs"
logger=logging.getLogger()
logger.setLevel("DEBUG")

console_handler=logging.StreamHandler()
console_handler.setLevel("DEBUG")

log_path=os.path.join(dir,"model_evaluation.log")
file_handler=logging.FileHandler(log_path)
file_handler.setLevel("DEBUG")


formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def load_model(path):
    try:
        with open(path, 'rb') as f:
            model = pickle.load(f)
        logger.debug("Model loaded successfully")
        return model
    except FileNotFoundError as e:
        logger.error("File is not found in provided directory %s",e)
        raise


def predict(model,data):
    try:
        preds=model.predict(data)
        return preds
    except FileNotFoundError as e:
        logger.error("File not found in directory %s",e)
        raise

def main():
    file_path=r"data\final\final_test.csv"
    model_path="models\model.pkl"
    test_data,test_labels=load_data(file_path)
    model=load_model(model_path)
    preds=predict(model,test_data)
    print(preds)
    

if __name__=="__main__":
    main()
    
    