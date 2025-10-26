from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator,PydanticUserError

from typing import List, Dict, Optional, Annotated

class User(BaseModel):

        name :str
        age:Annotated[int,Field(gt=0, lt=150 , description='Age must be between 0 and 150',strict=True)]
        married :bool
        allergies : Optional[List[str]]=None
        contact_info : Optional[Dict[str, str]]=None 
        website: AnyUrl
        email : EmailStr

        @field_validator('email')
        @classmethod
        def validate_email(cls, value):
            valid_domains = ['hdfc.com', 'icici.com']
            domain_name = value.split('@')[-1]
            if domain_name not in valid_domains:
                raise ValueError(f"Email domain must be one of {valid_domains}")
            return value
        
        @field_validator('name', mode='after') # mode='after' occurs after type coercion 
        @classmethod
        def capital_name(cls ,value):

            return value.upper()


patient_info={'name' : 'Anushka','age': 20,'married' : False,'allergies':['Chilli Flakes'],'email':'abc@icici.com','website':'https://www.example.com'}

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
 
 # field validators are used to validate and transform data at the field level
 # for depending fields in one model we use model_validator decorator
 # for example if we want to validate that age is greater than 18 if married is True
