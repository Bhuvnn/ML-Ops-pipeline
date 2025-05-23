import logging
import pandas as pd
import numpy as np
import nltk
nltk.download('punkt_tab')
import os
from sklearn.preprocessing import LabelEncoder

#creating logger
logger=logging.getLogger("Data Preprocessing")
logger.setLevel("DEBUG")

console_handler=logging.StreamHandler()
console_handler.setLevel("DEBUG")

log_path=os.path.join("logs","data_preprocessing.log")
file_handler=logging.FileHandler(log_path)
file_handler.setLevel("DEBUG")

formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") 
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def transform_text(text):
    """
    transforming,lowercasing,tokenizing our text.
    """
    stemmer=nltk.PorterStemmer()
    text=text.lower()
    text=nltk.word_tokenize(text)
    text=[word for word in text if word.isalnum()]
    text=[stemmer.stem(word) for word in text]
    return " ".join(text)

def preprocess_text(text,target,df):
    try:
        encoder=LabelEncoder()
        df[target]=encoder.fit_transform(df[target])
        logger.debug("Encoding completed")
        
        df=df.drop_duplicates(keep="first")
        logger.debug("Duplicate elements removed")
        
        df[text]=df[text].apply(transform_text)
        logger.debug("Transformation is completed")
        
        return df
    
    except KeyError as e:
        logger.exception("columns not found %s",e)
        raise

def main():
    try:
        train_df=pd.read_csv("data/train.csv")
        test_df=pd.read_csv("data/test.csv")
        logger.debug("Data Loaded Successfully")
        
        train_df=preprocess_text("text","target",train_df)
        test_df=preprocess_text("text","target",test_df)
        logger.debug("Data Preprocessed successfully")
        
        path=os.path.join("data","intermin")
        os.makedirs(path,exist_ok=True)
        
        train_df.to_csv(os.path.join(path,"preprocessed_train.csv"),index=False)   
        test_df.to_csv(os.path.join(path,"preprocessed_test.csv"),index=False) 
        logger.debug(f"Files saved at {path}")
    except FileNotFoundError as e:
        logger.error("file not found %s",e)
        raise
    
if __name__=="__main__":
    main()      
     
        
        
         
    

