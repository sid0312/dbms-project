from pymongo import MongoClient

import datetime

database_name = 'personal_diary'
collection_name = 'Notes'

collection = None

def create_connection():
    global collection
    client = MongoClient()
    db = client[database_name]
    collection = db[collection_name]

def insert_note(title,note,date):
    if collection is None:
        create_connection()
    doc = {
        'title': title,
        'note': note,
        'date': date
    }
    doc_id = collection.insert_one(doc).inserted_id
    print "Inserted document = {} with id = {}".format(doc, doc_id)

def find_all_notes():
    if collection is None:
        create_connection()
    doc_list = []
    for doc in collection.find():
        doc_list.append(doc)
    return doc_list

def delete_all_notes():
    if collection is None:
        create_connection()
    x = collection.delete_many({})
    print str(x.deleted_count) + "documents deleted."
