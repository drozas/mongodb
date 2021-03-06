
import pymongo
import sys

def find():
    # establish a connection to the database
    connection = pymongo.Connection("mongodb://localhost", safe=True)
    # get a handle to the school database
    db=connection.test
    images = db.images
    albums = db.albums

    print "find, reporting for duty"
    try:

        parented = []
        orphans = []
        total_kittens = 0
        parented_kittens = 0
        print 'Orphans ini'
        print len(orphans)
        print 'Parented ini'
        print len(parented)
        
        for image in images.find():
            #Count total number of kittens
            if 'kittens' in image['tags']:
                total_kittens = total_kittens + 1
                
            delete = True
            for album in albums.find():
                if image['_id'] in album['images']:
                    delete = False
            if delete == True:
                orphans.append(image)
            else:
                #Count total number of parented kittens
                if 'kittens' in image['tags']:
                    parented_kittens = parented_kittens + 1
                parented.append(image)
        

        print 'Orphans end'
        print len(orphans)
        print 'Parented end'
        print len(parented)
        print 'Total Kittens'
        print total_kittens
        print 'Parented Kittens'
        print parented_kittens
            
            
    except:
        print "Unexpected error:", sys.exc_info()[0]

find()