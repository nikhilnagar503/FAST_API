from pydantic import BaseModel,EmailStr,AnyUrl , Field
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,]
    age: int = Field(gt=10 ,lt = 65)
    email :EmailStr   # data_validation
    linkdinUrl : AnyUrl  # data_validation
    weight: float = None
    married: bool
    allegies: Optional[List[str]] = Field(max_length=5)
    contact_details: Optional[Dict[str, str]] = None  # Fixed typo & type

def insert_patient(patient: Patient):
    print(patient.age)
    print(patient.name)

patient_info = {
    'name': 'nitish',
    'age': 30,  # Don't use string for int
    'weight': 75.2,
    'married': False,
    'contact_details': {'phone': '2353462'}
}

patient1 = Patient(**patient_info)

if __name__ == "__main__":
    insert_patient(patient1)
