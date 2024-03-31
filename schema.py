from enum import Enum

# Define an Enum class for Disease Status
class DiseaseStatus(Enum):
    YES = "YES",
    NO = "NO"

# Define the schema for the data with types and enums where applicable
schema = {
    "age": int, # Age of the patient
    "sex": int, # Gender of the patient (0: Female, 1: Male)
    "cp": int, # Chest pain type
    "trestbps": int, # Resting blood pressure
    "chol": int, # Serum cholestoral in mg/dl
    "fbs": int, # Fasting blood sugar > 120 mg/dl (1: True, 0: False)
    "restecg": int, # Resting electrocardiographic results
    "thalach": int, # Maximum heart rate achieved
    "exang": int, # Exercise induced angina (1: Yes, 0: No)
    "oldpeak": float, # ST depression induced by exercise relative to rest
    "slope": int, # Slope of the peak exercise ST segment
    "ca": int, # Number of major vessels colored by fluoroscopy
    "thal": int, # Thalassemia
    "email": str, # Email of the patient
    "name":str, # Name of the patient
    "disease": DiseaseStatus # Disease status (YES/NO)
}
