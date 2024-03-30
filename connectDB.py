from pymongo import MongoClient

def connect_to_mongo():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['fastapi']
        print('Connected to MongoDB')
        return db
    except Exception as e:
        return {'error': str(e)}
    return db