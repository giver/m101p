import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)


def delete_student():
    db = connection.school
    try:
        cursor = db.students.find().sort([('_id', pymongo.ASCENDING)])
        #doc = grades.find({'type' : 'homework'})
        print cursor.count()

        # Iterate over scores student
        for doc in cursor:

            # set the highest number of int
            lowest_score = sys.maxint
            student_id = doc['_id']
            print 'student id =', student_id
            for score in doc['scores']:
                print 'current score = ', score['score']
                if lowest_score >= 0 and score['type'] == 'homework' and score['score'] < lowest_score:
                    lowest_score = score['score']
                elif lowest_score < 0:

                    # initial value lowest_score < 0
                    lowest_score = score['score']
            print 'lowest score =', lowest_score
            # since score not care about duplicate data
            print doc['scores']
            doc['scores'].remove({'type': 'homework', 'score': lowest_score})
            db.students.update({'_id': student_id}, {'$set': {'scores': doc['scores']}})
    except:
        print "Unexpected error:", sys.exc_info()[0]


def insert():
    # get a handle to the school database
    db = connection.school
    people = db.people

    print "insert, reporting for duty"

    richard = {"name": "Richard Kreuter", "company": "10gen",
               "interests": ['horses', 'skydiving', 'fencing']}
    andrew = {"_id": "erlichson", "name": "Andrew Erlichson", "company": "10gen",
              "interests": ['running', 'cycling', 'photography']}

    try:
        people.insert(richard)
        people.insert(andrew)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    print(richard)


delete_student()
