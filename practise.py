
import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)
print(LOG_FILE)
print(log_path)
print(LOG_FILE_PATH)