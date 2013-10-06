
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

def delete_student():
    db = connection.students
    print db
    grades = db.grades
    print grades
    last_id = -1

    print "Last id = ",last_id
    try:
        cursor = grades.find({'type' : 'homework'}).sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)])
        #doc = grades.find({'type' : 'homework'})
        print cursor
        for doc in cursor:
            if (doc['student_id'] != last_id):
                last_id = doc['student_id']
                print 'delete=',doc['_id']
                grades.remove(doc)
    except:
        print "Unexpected error:", sys.exc_info()[0]


def insert():

    # get a handle to the school database
    db=connection.school
    people = db.people

    print "insert, reporting for duty"

    richard ={"name":"Richard Kreuter", "company":"10gen",
              "interests":['horses', 'skydiving', 'fencing']}
    andrew = {"_id":"erlichson", "name":"Andrew Erlichson", "company":"10gen",
              "interests":['running', 'cycling', 'photography']}


    try:
        people.insert(richard)
        people.insert(andrew)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    print(richard)

delete_student()
