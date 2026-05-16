from shipment.logger import logging
from shipment.exception import shippingException
import sys
try:
    a=1/0
except Exception as e:
    logging.info("This is an error message")
    raise shippingException(e, sys)



logging.info("This is an info message")
