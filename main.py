from fastapi import FastAPI
import uvicorn
from connectDB import connect_to_mongo
from schema import HeartDisease
import pickle
import numpy as np

app = FastAPI()
db = connect_to_mongo()
collection = db["HeartDisease"]

filename = 'heart-disease-model.pkl'
model = pickle.load(open(filename, 'rb'))

@app.post('/store')
async def store(data: HeartDisease):
    
    try:
        data_dict = data.dict()
        collection.insert_one(data_dict)
    
        return {'message': 'Data stored successfully'}
    except Exception as e:
        return {'error': str(e)}
    
@app.post('/predict')
async def predict(data:dict):
    try:
        name = data.get("name","")
        x = collection.find_one({"name":name})
        # print(x['sex'])
        print(x)
        
        age = int(x['age'])
        sex = x['sex']
        cp = x['cp']
        trestbps = int(x['trestbps'])
        chol = int(x['chol'])
        fbs = x['fbs']
        restecg = int(x['restecg'])
        thalach = int(x['thalach'])
        exang = x['exang']
        oldpeak = float(x['oldpeak'])
        slope = x['slope']
        ca = int(x['ca'])
        thal = x['thal']
        
        model_input = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        output = model.predict(model_input)
        print(output)
        
        return {'message': 'Prediction successful'}
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    uvicorn.run(app)    
    