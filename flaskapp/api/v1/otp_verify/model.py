from pydantic import BaseModel,constr


from constants import PHONE_VALIDATION,EMAIL_VALIDATION

PhoneRegex =constr(regex=PHONE_VALIDATION)
EmailRegex =constr(regex=EMAIL_VALIDATION)

class Phone(BaseModel):
  phone: PhoneRegex


class PhoneVerify(BaseModel):
  phone: PhoneRegex
  otp:str

class Email(BaseModel):
  email: EmailRegex


class EmailVerify(BaseModel):
  email: EmailRegex
  otp:str