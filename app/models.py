# haven't seen a lot on how to structure the models page 
# for mongodb, just winging it for now

from app import mongo


# returns distinct channels
def getDistinctChannels():
    return mongo.db.channels.distinct('name')

