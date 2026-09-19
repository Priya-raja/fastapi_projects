from pydantic import BaseModel, field_validator

class PincodeRequest(BaseModel):
    pincode: str


    #pincode must be exactly 6 digits
    @field_validator("pincode")
    @classmethod

    def validate_pincode(cls,value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode must be exactly 6 digit")
        return value
