from pydantic import BaseModel, EmailStr, AnyUrl, Field

from typing import List, Dict, Optional, Annotated

# for data validation we use combination of Annotated and Field
# Annotated is used to add metadata to the field, while Field is used to set constraints
# to make field optional , we use field and annotated and set default value with what we want

class User(BaseModel):

    name :str
    age:Annotated[int,Field(gt=0, lt=150 , description='Age must be between 0 and 150',strict=True)]
    married :bool
    allergies : Optional[List[str]]=None
    contact_info : Optional[Dict[str, str]]=None # Optional fields need to be prvided with a default value here None
    
    # For data validation pydantic has EmailStr (for email validation), AnyURL(for links validation) 
    email: EmailStr
    website: AnyUrl

patient_info={'name' : 'Anushka','age': '20','married' : False,'allergies':['Chilli Flakes'],'email':'abc@gmail.com','website':'https://www.example.com'}

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
 


 # For usecase specific validation or transformation we can use @validator decorator :
