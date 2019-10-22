import os

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGO_URI = "mongodb+srv://root:tqElhg634c6ax5@myfirstcluster-yibrd.mongodb.net/myTestDB?retryWrites=true&w=majority"