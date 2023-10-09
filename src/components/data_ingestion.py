import os
import sys
sys.path.append('D:\VIT -COLLEGE\TY_\sem1\EDI\git_repo_ADITYA_M\signlanguage_NLPproject')

#un comment the below part later...
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# # #comment this section later
# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exc_info()
#     file_name=exc_tb.tb_frame.f_code.co_filename
#     error_message="Error occured in python script name[{0}] line number[{1}] error message[{2}]".format(
#     file_name, exc_tb.tb_lineno, str(error))

#     return error_message
# class CustomException(Exception):
#     def __init__(self, error_message, error_detail:sys):
#         super().__init__(error_message)
#         self.error_message=error_message_detail(error_message, error_detail=error_detail)

#     def __str__(self):
#         return self.error_message

# #comment the above section later

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')                #only hv to change this line of code to get data from anywhere.
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()


