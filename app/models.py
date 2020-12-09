# haven't seen a lot on how to structure the models page 
# for mongodb, just winging it for now
# this is a collection of queries I use throughout the rest of the app

from app import mongo


# returns distinct channels
def get_distinct_channels():
    return mongo.db.channels.distinct('name')

# returns channel id given a channel name
def get_channel_id(channel_name):
    return mongo.db.channels.find_one({"name": channel_name})['id']

# returns user id
def get_user_id(username):
    user_id = mongo.db.users.find_one({"profile.display_name": username})
    
    # if user is not found, return None
    if user_id == None:
        return None
    elif user_id != None:
        return user_id['id']

# return username
def get_user_name(user_id):
    username = mongo.db.users.find_one({"id": user_id})

    # if user is not found, return None
    if username == None:
        return None
    elif username != None:
        return username['profile']['display_name']