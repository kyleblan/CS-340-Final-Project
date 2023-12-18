# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter(object):

#Initialize, name variables
    def __init__(self):
        
        #URI must be percent escaped as per pymongo documentation
        username = urllib.parse.quote_plus('aacuser')
        password = urllib.parse.quote_plus('testing123')
        host = urllib.parse.quote_plus('nv-desktop-services.apporto.com')
        port = 30103
        
        self.client = MongoClient("mongodb://%s:%s@%s:%d/?authSource=AAC" % (username, password, host, port))
        self.dataBase = self.client['AAC']
        
#Create method    
    def create(self, data):
       if data is not None:
           insertValid = self.dataBase.animals.insert_one(data)
           #check the status of the inserted value 
           return True if insertValid.acknowledged else False

       else:
           raise Exception("No document to save. Data is empty.")

#Read method    
    def read(self, data):
            output = self.dataBase.animals.find(data,{'_id': False})
            return output
    
#Update method
    def update(self, initial, change):
        if initial is not None:
            update_result = self.dataBase.animals.update_many(initial, {"$set": change})
            result = update_result.raw_result
        
            return result
        else:
            raise Exception("Nothing to update, data parameter is empty")

#Delete method      
    def delete(self, remove):
        if remove is not None:
            delete_result = self.dataBase.animals.delete_many(remove)
            result = delete_result.raw_result
         
            return result
        else:
            raise Exception("Nothing to update, data parameter is empty")