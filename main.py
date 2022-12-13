import os,sys
from finance_complaint.constant.environment.variable_key import AWS_ACCESS_KEY_ID_ENV_KEY,AWS_SECRET_ACCESS_KEY_ENV_KEY
from dotenv import load_dotenv
load_dotenv()
access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY,)
secret_access_key =os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY,)

import argparse
from finance_complaint.exception import FinanceException
from finance_complaint.logger import logger


def start_training(start=False):
    try:
        if not start:
            return None
        print("Training Running")
    
    except Exception as e:
        raise FinanceException(e, sys)