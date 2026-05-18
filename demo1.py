from shipment.configuration.mongo_operations import MongoDBOperation
from shipment.utils.main_utils import MainUtils
obj = MongoDBOperation()
db_name = "ShipmentDB"
collection_name = "shipment_collection"
df = obj.get_collection_as_dataframe(db_name, collection_name)
print(df.head())