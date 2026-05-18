"""from shipment.logger import logging
from shipment.exception import shippingException
from shipment.utils.main_utils import MainUtils
import sys
try:
    a=1/0
except Exception as e:
    logging.info("This is an error message")
    raise shippingException(e, sys)



logging.info("This is an info message")

obj = MainUtils()
data=obj.yml_file_path = "config/model.yaml"
print(obj.read_yaml_file(data))
"""
from shipment.pipline.training_pipeline import TrainPipeline

obj=TrainPipeline()
obj.run_pipeline()

