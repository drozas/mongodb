
import pymongo
from decimal import Decimal
import sys

def find():
    # establish a connection to the database
    connection = pymongo.Connection("mongodb://localhost", safe=True)
    # get a handle to the school database
    db = connection.school
    students = db.students

    print "find, reporting for duty"

    try:
        for student in students.find():
            print student
            hw_scores = []
            new_scores = []
            for score in student['scores']:
                #get all the scores related to homework of that user, add the rest to the new list
                if score['type'] == 'homework':
                    hw_scores.append(score['score'])
                else:
                    new_scores.append({"type" : score['type'], "score" : score['score']})
            
            #Remove the minimun value from the HW group
            hw_scores.remove(min(hw_scores))
            #Add the rest of hw scores to the new group
            for hw_score in hw_scores:
                new_scores.append({"type" : "homework", "score" : hw_score})
                
            #Assign the new scores to that student and update it
            student['scores'] =  new_scores
            print student
            students.save(student)
            



    except:
        print "Unexpected error:", sys.exc_info()[0]

find()
