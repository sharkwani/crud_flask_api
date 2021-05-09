from flask import Flask  , request , Response
import json 
from  file_processing import fileProcessing  
from database import Database  as mongoDb

from file_type import FileType
FileTypeNum = { "song" : 1,
            "podcast": 2,
            "audiobook" : 3 }
app = Flask(__name__)

def send_response(response):
            if response == "success":
               return  Response(
                response = json.dumps({ "message":  "Action is successful"
                                       }) ,
                status = 200,
                mimetype ="application/json")
            elif response == "already in db":
                return  Response(
                response = json.dumps({ "message":  "Already same record exits"
                                       }) ,
                status = 200,
                mimetype ="application/json")
            elif response =="mandatry field not found":
                return  Response(
                response = json.dumps({ "message":  "one or more mandatory field absent"
                                       }) ,
                status = 200,
                mimetype ="application/json")
            else:
               return  Response(
                response = json.dumps({ "message":  "Internal error"
                                       }) ,
                status = 500,
                mimetype ="application/json")
               
@app.route('/add'  , methods=["POST"])
def add_file_to_db():
        audioType = request.args.get("audioType").lower()
        if audioType.lower() not in FileTypeNum.keys():
            return Response(
                response = json.dumps({ "message":  "The request is invalid"
                                       }) ,
                status = 400,
                mimetype ="application/json")
        metaData = request.get_json()
        
        if FileType.Song.value== FileTypeNum[audioType] :
            response = fileProcessing(metaData).song()
            return send_response(response)
        elif FileTypeNum[audioType] == FileType.Podcast.value:
                response =  fileProcessing(metaData).podCast()
                return send_response(response)
        elif FileTypeNum[audioType]  == FileType.Audiobook.value:
             response =  fileProcessing(metaData).audioBook()
             return send_response(response)
            
        else:
            return  Response(
                response = json.dumps({ "message":  "The request is invalid"
                                       }) ,
                status = 400,
                mimetype ="application/json")




@app.route('/fetch/<type>'  , methods=["GET"])        
@app.route('/fetch/<type>/<int:id>'  , methods=["GET"])
def get_document_by_id(type,id=None):
    if type.lower() not in FileTypeNum.keys():
        return  Response(
                response = json.dumps({ "message":  "The request is invalid , please specify a proper audiotype"
                                       }) ,
                status = 400,
                mimetype ="application/json")
    
    dbObj = mongoDb(type)
    if id == None :
        
        results = dbObj.fetch_data()
        if results["dbCode"]  != None :
                return Response(
                                response =  results["dbMessage"] , 
                                status = 200 ,
                                mimetype = "application/json"
                                
                                )
        return Response(
                                response = json.dumps({ "Data":   results["dbMessage"] }) , 
                                status = results["statusCode"] ,
                                mimetype = "application/json"
                                
                                )
    else:
       results = dbObj.fetch_data(id)
       if results["dbCode"]  != None :
                return Response(
                                response =  results["dbMessage"] , 
                                status = 200 ,
                                mimetype = "application/json"
                                
                                )
       return Response(
                                response = json.dumps({ "Data":   results["dbMessage"] }) , 
                                status = results["statusCode"] ,
                                mimetype = "application/json"
                                
                                )




@app.route('/delete/<type>/<int:id>'  , methods=["DELETE"])
def delete_record(type , id):
    if type.lower() not in FileTypeNum.keys():
        return  Response(
                response = json.dumps({ "message":  "The request is invalid , please specify a proper audiotype"
                                       }) ,
                status = 400,
                mimetype ="application/json")
  
    dbObj = mongoDb(type)
    response = dbObj.delete_record(id)
    if response == 1:
          return  Response(
                response = json.dumps({ "message":  f"Record with id : {id} deleted"
                                       }) ,
                status = 200,
                mimetype ="application/json")   
    elif response == 0:
         return  Response(
                response = json.dumps({ "message":  f"Record with id : {id} not found"
                                       }) ,
                status = 200,
                mimetype ="application/json")   
   
    else:
        return  Response(
                response = json.dumps({ "message": "Internal error"
                                       }) ,
                status = 500,
                mimetype ="application/json")





@app.route('/update/<type>/<int:id>'  , methods=["PATCH"])
def update_record(type , id):

        if type.lower() not in FileTypeNum.keys():
            return  Response(
                    response = json.dumps({ "message":  "The request is invalid , please specify a proper audiotype"
                                        }) ,
                    status = 400,
                    mimetype ="application/json")
        dbObj = mongoDb(type)
        metaData = request.get_json()
        response = dbObj.update_record(id,  metaData)
        if response == 1:
            return  Response(
                    response = json.dumps({ "message":  f"Record with id : {id} modified"
                                        }) ,
                    status = 200,
                    mimetype ="application/json")   
        elif response == 0:
            return  Response(
                    response = json.dumps({ "message":  f"Record with id : {id} has nothing to update"
                                        }) ,
                    status = 200,
                    mimetype ="application/json")   
    
        else:
            return  Response(
                    response = json.dumps({ "message": "Internal error"
                                        }) ,
                    status = 500,
                    mimetype ="application/json")
if __name__ == '__main__':
    app.run(debug=True)