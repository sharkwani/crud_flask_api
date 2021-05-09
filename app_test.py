import unittest
import requests as req

class ApiTesting(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"
    
    
    post_link = f"{API_URL}/add?audioType=song"
    wrong_post_link = f"{API_URL}/add?audioType=wrong"
    
    get_url = f"{API_URL}/fetch/song"
    wrong_get_url = f"{API_URL}/fetch/sog"
    
    delete_url = f"{API_URL}/delete/song/456"
    wrong_delete_url = f"{API_URL}/delete/sog/456"
    
    update_url = f"{API_URL}/update/song/456"
    wrong_update_url = f"{API_URL}/update/sog/456"
    
    
    post_link__metadata ={
   "ID" :456,
    "Name of the song" :"hello" ,
    "Duration" :456,
    "Uploaded time":1234}
    wrong_post_link__metadata ={
   "ID" :4565,
    #"Name of the song" :"hello" , #skipping one mandatory entry 
    "Duration" :456,
    "Uploaded time":1234}
    
    
    update_link__metadata ={
   "ID" :456,
    "Name of the song" :"hellox" ,
    "Duration" :456,
    "Uploaded time":1234}
    ######################################### POST REQUEST TESTCASES ###################################################### 
    def test_case_1_post_a_record(self):
        response = req.post(self.post_link , json = self.post_link__metadata)
        self.assertEqual(response.status_code, 200)
        
        
    def test_case_2_post_a_record_negative(self):
        response = req.post(self.post_link , json = self.wrong_post_link__metadata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "one or more mandatory field absent")
    
    
    def test_case_3_post_a_record_sameID_negative(self):
        response = req.post(self.post_link , json = self.post_link__metadata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"],  "Already same record exits")    
    
    
    def test_case_4_post_a_record_audiotype_negative(self):
        response = req.post(self.wrong_post_link , json = self.wrong_post_link__metadata)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"],  "The request is invalid")   
    ######################################### POST REQUEST TESTCASES ######################################################    
    
    ######################################### GET REQUEST TESTCASES ###################################################### 
    def test_case_5_get_all_records(self):
        response = req.get(self.get_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()) ,list)
    
    
    def test_case_6_get_a_record_with_id(self):
        response = req.get(f"{self.get_url}/456")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()) ,dict)
    
    
    def test_case_7_get_norecordfound(self):
        response = req.get(f"{self.get_url}/4567")
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(response.json()["Data"] ,"No record found")
    
    
    def test_case_8_get_a_record_audiotype_negative(self):
        response = req.get(f"{self.wrong_get_url}/456")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"],   "The request is invalid , please specify a proper audiotype")    
    ######################################### GET REQUEST TESTCASES ######################################################     

    
    ######################################### DELETE REQUEST TESTCASES ###################################################### 

    def test_case_9_delete_a_record_invalid_type(self):
        response = req.delete(self.wrong_delete_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"],   "The request is invalid , please specify a proper audiotype")  
    
    
    @unittest.SkipTest #Remove this to delete an entry 
    def test_case_10_delete_a_record(self):
        response = req.delete(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"],  "Record with id : 456 deleted")      
    
    @unittest.SkipTest
    def test_case_11_delete_record_not_found(self):
        response = req.delete(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"],  "Record with id : 456 not found")      

    ######################################### DELETE REQUEST TESTCASES ###################################################### 


    ######################################### UPDATE REQUEST TESTCASES ###################################################### 
    def test_case_12_update_a_record_invalid_type(self):
        response = req.patch(self.wrong_update_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"],   "The request is invalid , please specify a proper audiotype")
    def test_case_14_update_a_record_not_found(self):
        response = req.patch(self.update_url , json = self.update_link__metadata )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"],  "Record with id : 456 modified")        
    
    def test_case_15_update_a_record_not_found(self):
        response = req.patch(self.update_url , json = self.update_link__metadata )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"],  "Record with id : 456 has nothing to update")    
  
  
  
  
  
    ######################################### UPDATE REQUEST TESTCASES ###################################################### 
if __name__ == "__main__":
    unittest.main()