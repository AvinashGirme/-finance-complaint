import os,sys
import re
import time
import uuid
from collections import namedtuple
from typing import List

import json
import pandas as pd 
import requests

from finance_complaint.config.pipeline.training import FinanceConfig
from finance_complaint.entity.artifact_entity import DataIngestionArtifact
from finance_complaint.entity.config_entity import DataIngestionConfig
from finance_complaint.entity.metadata_entity import DataIngestionMetadata
from finance_complaint.exception import FinanceException
from finance_complaint.logger import logger
from datetime import datetime
from finance_complaint.config.spark_manager import spark_session

DownloadUrl=namedtuple("DownloadUrl", ["url","file_path","n_retry"])

class DataIngestion:
    #used to download data in chunks.
    def __init__(self,data_ingestion_config:DataIngestionConfig,n_retry: int =5,):
        """
        data_ingestion_config: Data Ingestion Config
        n_retry: Number of retry filed should be tried to download in case of failure encountered
        n_month_interval: n month data will be downloaded 
        """

        try:
            logger.info(f"{'>>' * 20} Starting Data Ingestion {'<<' * 20}")
            self.data_ingestion_config=data_ingestion_config
            self.failed_download_urls: List[DownloadUrl] = []
            self.n_retry=n_retry
            
        except Exception as e:
            raise FinanceException(e, sys)
            



