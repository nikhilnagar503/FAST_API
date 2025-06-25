from fastapi import FastAPI,HTTPException,Query
app = FastAPI()
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal


class patients(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]



    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'
    

def load_data():
    with open("patients.json",'r') as f:
        data = json.load(f)
    return data


def save_data(data):
     with open("patients.json",'w') as f:
        json.dump(data,f)


@app.get("/")

def hello():
    return {'message':'hello world'}


@app.get("/about")
def about():
    return {"hello my name is nikhil how are you "}



@app.get("/view")
def view():
    data = load_data()

    return data



@app.get("/patient/{patient_id}")
def patient_id(patient_id:str):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="data not found")



@app.get("/sort")
def sort_patients(sort_by:str = Query(...,description="sort on the basis of height,weight,bmi"),order:str = Query('asc',description="sort in asc and desc order")):
    valid_field = ['height','weight','bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code=400,detail='invalid field select the valid field {from valid field }')
    


    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,description = "invalid order please select the valid  order  " )
    


    data = load_data()
    sort_order = True if order == 'desc' else  False
    sorted_data = sorted(data.values(),key=lambda x : x.get(sort_by,0),reverse=sort_order)

    return sorted_data






@app.post("/create")

def create_patients(patients:patients):
    data = load_data


    if patient_id.id in data:
        raise HTTPException(status_code = 400,detail='Patient already exists')
    
    data[patients.id] = patients.model_dump(exclude=['id'])

    save_data(data)


    return JSONResponse(status_code=201, content={'message':'patient created successfully'})


@app.put("update")



