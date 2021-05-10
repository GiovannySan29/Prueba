from flask import Flask, render_template,request,redirect,url_for # For flask implementation    
from bson import ObjectId # For ObjectId to work    
from pymongo import MongoClient    
import os    
    
app = Flask(__name__)    
title = "TODO sample application with Flask and MongoDB"    
heading = "TODO Reminder with Flask and MongoDB"    
    
client = MongoClient("mongodb://127.0.0.1:27017") #host uri    
db = client.renta    #Select the database    
collection = db.Users #Select the collection name    
    
def redirect_url():    
    return request.args.get('next') 
    request.referrer   
    url_for('index')    
  
@app.route("/list")    
def lists ():    
    #Display the all Tasks    
    collection_l = collection.find()    
    a1="active"    
    return render_template('index.html',a1=a1,collection=collection_l,t=title,h=heading)    
  
@app.route("/")    
@app.route("/uncompleted")    
def tasks ():    
    #Display the Uncompleted Tasks    
    collection_l = collection.find({"done":"no"})    
    a2="active"    
    return render_template('index.html',a2=a2,collection=collection_l,t=title,h=heading)    
  
  
@app.route("/completed")    
def completed ():    
    #Display the Completed Tasks    
    collection_l = collection.find({"done":"yes"})    
    a3="active"    
    return render_template('index.html',a3=a3,collection=collection_l,t=title,h=heading)    
  
@app.route("/done")    
def done ():    
    #Done-or-not ICON    
    id=request.values.get("_id")    
    task=collection.find({"_id":ObjectId(id)})    
    if(task[0]["done"]=="yes"):    
        collection.update({"_id":ObjectId(id)}, {"$set": {"done":"no"}})    
    else:    
        collection.update({"_id":ObjectId(id)}, {"$set": {"done":"yes"}})    
    redir=redirect_url()        
    
    return redirect(redir)    
  
@app.route("/action", methods=['POST'])    
def action ():    
    #Adding a Task    
    name=request.values.get("name")    
    desc=request.values.get("desc")    
    date=request.values.get("date")    
    pr=request.values.get("pr")    
    collection.insert({ "name":name, "desc":desc, "date":date, "pr":pr, "done":"no"})    
    return redirect("/list")    
  
@app.route("/remove")    
def remove ():    
    #Deleting a Task with various references    
    key=request.values.get("_id")    
    collection.remove({"_id":ObjectId(key)})    
    return redirect("/")    
  
@app.route("/update")    
def update ():    
    id=request.values.get("_id")    
    task=collection.find({"_id":ObjectId(id)})    
    return render_template('update.html',tasks=task,h=heading,t=title)    
  
@app.route("/action3", methods=['POST'])    
def action3 ():    
    #Updating a Task with various references    
    name=request.values.get("name")    
    desc=request.values.get("desc")    
    date=request.values.get("date")    
    pr=request.values.get("pr")    
    id=request.values.get("_id")    
    collection.update({"_id":ObjectId(id)}, {'$set':{ "name":name, "desc":desc, "date":date, "pr":pr }})    
    return redirect("/")    
  
@app.route("/search", methods=['GET'])    
def search():    
    #Searching a Task with various references    
    
    key=request.values.get("key")    
    refer=request.values.get("refer")    
    if(key=="_id"):    
        collection_l = collection.find({refer:ObjectId(key)})    
    else:    
        collection_l = collection.find({refer:key})    
    return render_template('searchlist.html',collection=collection_l,t=title,h=heading)    
    
if __name__ == "__main__":    
    
    app.run()   