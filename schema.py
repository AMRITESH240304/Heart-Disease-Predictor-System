from pydantic import BaseModel

class HeartDisease(BaseModel):
    name:str
    age: int
    sex: str
    cp: str
    trestbps: int
    chol: int
    fbs: str
    restecg: int
    thalach: int
    exang: str
    oldpeak: float
    slope: str
    ca: int
    thal: str
