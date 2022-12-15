import os,sys
from collections import namedtuple
from typing import List,Dict
from pyspark.sql import DataFrame
from pyspark.sql.functions import col

from finance_complaint.config.spark_manager import spark_session
from finance_complaint.entity.artifact_entity import DataIngestionArtifact
from finance_complaint.entity.config_entity import DataValidationConfig
from finance_complaint.entity.schema import FinanceDataSchema
from finance_complaint.exception import FinanceException
from finance_complaint.logger import logger

from pyspark.sql.functions import lit
from finance_complaint.entity.artifact_entity import DataValidationArtifact

COMPLAINT_TABLE = "complaint"
ERROR_MESSAGE="error_msg"
MissingReport= namedtuple('MissingReport', ["total_row","missing_row","missing_percentage"])



