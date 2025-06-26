from pydantic import basemodel ,EmailStr,field_validator
from typing import Optional,list,Dict

class patients(basemodel):
    name : str
    age : int 
    email : EmailStr
    weight : float
    married : bool
    allergies : list[str]
    contact_details : dict[str,str]


    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icici.com']

        domain_name = value.split('@')[-1]


        if domain_name not in domain_name :
            raise ValueError("not a valid domain")
        

        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    

    @field_validator("age",mode="after")
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else: raise ValueError("age should be between 0 and 100")



def update_patient_data(patient: patients):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = patients(**patient_info) # validation -> type coercion

update_patient_data(patient1)




