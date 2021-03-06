
import pymongo
import sys

def find():
	# establish a connection to the database
	connection = pymongo.Connection("mongodb://localhost", safe=True)
	# get a handle to the school database
	db=connection.students
	grades = db.grades

	print "find, reporting for duty"
	query = {'type':'homework'}
	try:
		cursor = grades.find(query)
        	cursor = cursor.sort([('student_id', pymongo.ASCENDING),('score', pymongo.DESCENDING)])
		prev_student_id = 0
		prev_grade_id = ""

    		for grade in cursor:
			print grade
			print prev_grade_id
			print prev_student_id
			#Delete previous grade if this is a new student
			if grade['student_id'] != prev_student_id:
				grades.remove({'_id' : prev_grade_id})

			prev_student_id = grade['student_id']
			prev_grade_id = grade['_id']
      
	except:
		print "Unexpected error:", sys.exc_info()[0]

find()
