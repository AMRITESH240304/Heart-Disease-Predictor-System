import pickle
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from connectDB import connect_to_mongo
from schema import schema

app = FastAPI()

# Allowing CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connecting to MongoDB
db = connect_to_mongo()
collection = db["HeartDisease"]

# Loading the trained model
filename = 'heart-disease-model.pkl'
with open(filename, 'rb') as file:
    model = pickle.load(file)

@app.post("/store")
async def store(data: dict):
    try:
        email = data.get('email', '')
        
        # Checking if email already exists
        if collection.find_one({"email": email}):
            return {"message": "Data already exists"}
        
        # Validating and inserting data into MongoDB
        converted_data = {key: schema[key](value) for key, value in data.items()}
        collection.insert_one(converted_data)
        
        return {"message": "Data received successfully"}
    except Exception as e:
        return {'error': str(e)}
    
@app.post('/predict')
async def predict(data: dict):
    try:
        email = data.get("email", "")
        x = collection.find_one({"email": email})
        
        # Checking if data exists if not raise 404 error
        if x is None:
            raise HTTPException(status_code=404, detail="Data not found")
        
        # Extracting features for prediction
        features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        model_input = np.array([[x[feature] for feature in features]])
        
        # Making prediction
        output = model.predict(model_input)
        
        # Updating MongoDB with prediction result
        disease_status = "YES" if output[0] == 1 else "NO"
        collection.update_one({"email": email}, {"$set": {"disease": disease_status}})
        
        return JSONResponse(content={'output': int(output[0])})
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
