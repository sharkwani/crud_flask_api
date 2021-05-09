import pymongo
mongo = pymongo.MongoClient(
    host = "localhost",
    port = 27017,
    serverSelectionTimeoutMs = 1000
)
db = mongo.files
class fileProcessing:
        def __init__(self,metaData):
                self.metaData = metaData
        
        
        
        
        def validate_data_song(self,collection):
             if not collection.find({"ID": self.metaData["ID"]}).count() == 0:
                 return 0
             if "ID" not in self.metaData.keys() or "Name of the song" not in self.metaData.keys() or  "Duration" not in self.metaData.keys() or "Uploaded time" not in self.metaData.keys():
                 return 1
 
             return 2   



       
       
        def validate_data_podcast(self,collection):
             if not collection.find({"ID": self.metaData["ID"]}).count() == 0:
                 return 0
             if "ID" not in self.metaData.keys() or "Name of the song" not in self.metaData.keys() or  "Duration" not in self.metaData.keys() or "Uploaded time" not in self.metaData.keys():
                 return 1
 
             return 2  
        
        
        def validate_data_audiobook(self,collection):
             if not collection.find({"ID": self.metaData["ID"]}).count() == 0:
                 return 0
             if "ID" not in self.metaData.keys() or "Name of the song" not in self.metaData.keys() or  "Duration" not in self.metaData.keys() or "Uploaded time" not in self.metaData.keys():
                 return 1
 
             return 2  
        
        
        
        def song(self):
            
                validResponse = self.validate_data_song(db.song) 
                if validResponse == 2:
                    db.song.insert_one(self.metaData)
                   
                    return "success"
                elif validResponse == 0 :
                    return "already in db"
                elif validResponse == 1 :
                    return "mandatry field not found"
           
                return "failure"
        
        
        def podCast(self):
            try:
                if self.validate_data_podcast(db.podCast):
                    db.podCast.insert_one(self.metaData)
                    
                    return "success"
                else:
                    return "already in db"
            except:
                return "failure"
            
        
        def audioBook(self):
            try:
                if self.validate_data_audiobook(db.audioBook):
                    db.audioBook.insert_one(self.metaData)
                    
                    return "success"
                else:
                    return "already in db"
            except:
                return "failure"
            
        
            