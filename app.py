from fastapi import FastAPI
from pydantic import BaseModel, Field
import pickle
import pandas as pd
from fastapi.responses import JSONResponse

app = FastAPI()

with open('DiabetesModel.pkl', 'rb') as f:
 model = pickle.load(f)

class UserInput(BaseModel):

  Pregnancies: int | None = Field(..., description='No of pregnancies the patient had had')
  Glucose: int = Field(..., gt=0, description='The glucose level as tested')
  BloodPressure: int = Field(..., gt=0, description='The patient blood pressure as tested')
  SkinThickness: int = Field(...,gt=0, description='The result of the skin thickness measure')
  Insulin: int = Field(..., description='The patient insulin level')
  BMI: float = Field(...,gt=0, description='The calculated bmi of the patient')
  DiabetesPedigreeFunction: float = Field(...,gt=0, description='the patient diabetes pedigree function as tested')
  Age: int = Field(..., gt=0, lt=120, description='The patient age')


@app.post('/predict')
def predict_diabetes(data: UserInput):

  input_df = pd.DataFrame([{
    'Pregnancies': data.Pregnancies,
    'Glucose': data.Glucose,
    'BloodPressure': data.BloodPressure,
    'SkinThickness': data.SkinThickness, 
    'Insulin': data.Insulin,
    'BMI': data.BMI,
    'DiabetesPedigreeFunction': data.DiabetesPedigreeFunction,
    'Age': data.Age
   }])

  prediction = int(model.predict(input_df))

  return JSONResponse(
        status_code=200,
        content={
            'message': "Diabetic" if prediction == 1 else "Not Diabetic"
        }
    )