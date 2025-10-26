from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator

from typing import List, Dict, Optional, Annotated



class User(BaseModel):

    name :str
    age: Annotated[int,Field(gt=0, lt=150 , description='Age must be between 0 and 150',strict=True)]
    married :bool
    allergies : Optional[List[str]]=None
    contact_info : Dict[str, str]  
    email: EmailStr
    website: AnyUrl

    @model_validator(mode='after')
    def emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_info:
            raise ValueError("Emergency contact is required for patients above 60 years of age")
        return model


patient_info={'name' : 'Anushka','age': 65,'married' : False,'allergies':['Chilli Flakes'],'contact_info': {'phone': '1234567890'},'email':'abc@gmail.com','website':'https://www.example.com'}

patient1=User(**patient_info)

def insert_patient_info(patient : User):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_info)
    print(patient.email)
    print(patient.website)
    print("Sucessfully inserted patient info")

insert_patient_info(patient1)
