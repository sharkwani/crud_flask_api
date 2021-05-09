import pymongo
import json
mongo = pymongo.MongoClient(
    host = "localhost",
    port = 27017,
    serverSelectionTimeoutMs = 1000
)
db = mongo["files"]
class Database:
        def __init__(self , collection):
                self.collection = collection
        def helper_fetch_record_fromdb(self , collectionToUse , id =None , ):
                if id == None:
                       try:
                            cursor = collectionToUse.find({})
                            records= []
                            for record in cursor: 
                                del record["_id"] 
                                records.append(record)
                            print(records)
                            if records == []:
                                return {
                                    "dbCode": None ,
                                    "statusCode" : 200 ,
                                    "dbMessage" :"DataBase Empty"
                                    
                                    
                                }
                            return {
                                    "dbCode": 1 ,
                                    "statusCode" : 200 ,
                                    "dbMessage" : json.dumps(records , default=str)
                                    
                                    
                                }
                       except:
                           return {
                                    "dbCode": None ,
                                    "statusCode" : 500 ,
                                    "dbMessage" : "Internal error"
                                    
                                    
                                }
                           
                else:       
                        try:
                            cursor = collectionToUse.find_one({"ID":id})
                            if cursor :
                                del cursor["_id"]
                                return {
                                    "dbCode": 1 ,
                                    "statusCode" : 200 ,
                                    "dbMessage" : json.dumps(cursor , default=str)
                                    
                                    
                                }
                            return {
                                    "dbCode": None ,
                                    "statusCode" : 200 ,
                                    "dbMessage" :"No record found"
                                    
                                    
                                }
                        except:
                               return {
                                    "dbCode": None ,
                                    "statusCode" : 500 ,
                                    "dbMessage" : "Internal error"
                                    
                                    
                                }
        def fetch_data(self, id = None):
            if self.collection.lower() == "song":
                collectionObj = db["song"]
                return self.helper_fetch_record_fromdb(collectionObj,id)

            elif self.collection.lower() == "podcast":
                collectionObj = db["podCast"]
                return self.helper_fetch_record_fromdb(collectionObj,id)
            else:
                collectionObj = db["audioBook"]
                return self.helper_fetch_record_fromdb(collectionObj,id)
        def delete_record(self,id):
            if self.collection.lower() == "song":
                collectionObj = db["song"]
                try:
                    response = collectionObj.delete_one({"ID":id})
                    if response.deleted_count ==1:
                            return 1
                    else :
                            return 0
                except:
                    return -1
                
                
            elif self.collection.lower() == "podcast":
                collectionObj = db["podCast"]
                try:
                    response = collectionObj.delete_one({"ID":id})
                    if response.deleted_count ==1:
                            return 1
                    else :
                            return 0
                except:
                    return -1
            else:
                collectionObj = db["audioBook"]
                try:
                    response = collectionObj.delete_one({"IDL":id})
                    if response.deleted_count ==1:
                            return 1
                    else :
                            return 0
                except:
                    return -1
        def update_record(self , id , updatedRecord):
            if self.collection.lower() == "song":
                collectionObj = db["song"]
                try:
                    response = collectionObj.update_one({"ID":id},
                                                        
                                                        {"$set":updatedRecord}
                                                        
                                                        )
                    if response.modified_count ==1:
                            return 1
                    else :
                            return 0
                except:
                    return -1
                
                
            elif self.collection.lower() == "podcast":
                collectionObj = db["podCast"]
                try:
                    response = collectionObj.update_one({"ID":id},
                                                        
                                                        {"$set":updatedRecord}
                                                        
                                                        )
                    if response.modified_count ==1:
                            return 1
                    else :
                            return 0
                except:
                    return -1
            else:
                collectionObj = db["audioBook"]
                try:
                    response = collectionObj.update_one({"ID":id},
                                                        
                                                        {"$set":updatedRecord}
                                                        
                                                        )
                    if response.modified_count ==1:
                            return 1
                    else :
                            return 0
                except:
                    return -1           
