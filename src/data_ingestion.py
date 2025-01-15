import numpy as np
import pandas as pd
import os
import logging
import sklearn.model_selection import train_test_split

log_dir = 'logs'
os.makedirs(log_dir, exist_ok='True')

logger = logging.getLogger('data_integration')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'data_ingestion.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)



df = pd.read_csv('')