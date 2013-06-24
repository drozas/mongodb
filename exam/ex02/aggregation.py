
import pymongo
import sys

def find():
    # establish a connection to the database
    connection = pymongo.Connection("mongodb://localhost", safe=True)
    # get a handle to the school database
    db=connection.enron
    messages = db.messages

    print "find, reporting for duty"
    try:
        #Remove all the duplicates
        messages_filtered = []
        for m in messages.find(None, {"headers.From":True,"headers.To":True,"_id":True}):
            m2 = {}
            if "To" in m['headers']:
                m2['from'] = m['headers']['From']
                m2['to'] = set(m['headers']['To'])

            messages_filtered.append(m2)
        
        #Generate all possible combinations
        combination = set()
        for m in messages_filtered:
            print m
            if ("from" in m) & ("to" in m):
                print m["from"]
                print m["to"]
                #for to in m["to"]:
                #    combination.add({m["from"], to})
                    

    except:
        print "Unexpected error:", sys.exc_info()[0]

find()