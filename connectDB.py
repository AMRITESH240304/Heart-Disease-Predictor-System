from pymongo import MongoClient

def connect_to_mongo():
    try:
        # Connect to MongoDB server
        client = MongoClient('mongodb://localhost:27017/')
        
        # Access or create the 'fastapi' database
        db = client['fastapi']
        
        # Print a success message
        print('Connected to MongoDB')
        
        # Return the database object
        return db
    except Exception as e:
        return {'error': str(e)}
    return db