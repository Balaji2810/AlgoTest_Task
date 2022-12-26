from pydantic import BaseModel,constr

from constants import PHONE_VALIDATION,EMAIL_VALIDATION,NAME_VALIDATION,PASSWORD_VALIDATION,PHONE_OR_EMAIL_VALIDATION

PhoneRegex =constr(regex=PHONE_VALIDATION)
EmailRegex =constr(regex=EMAIL_VALIDATION)
PhoneOrEmailRegex = constr(regex=PHONE_OR_EMAIL_VALIDATION)
NameRegex =constr(regex=NAME_VALIDATION)
PasswordRegex =constr(regex=PASSWORD_VALIDATION)

class SignUp(BaseModel):
  phone: PhoneRegex
  email:EmailRegex
  email_otp:str
  phone_otp:str
  name:NameRegex
  password:PasswordRegex

class Login(BaseModel):
  phone_or_email: PhoneOrEmailRegex
  password:PasswordRegex

class ForgetPassword(BaseModel):
  phone_or_email: PhoneOrEmailRegex
  new_password:PasswordRegex
  otp:str

class Check(BaseModel):
  phone_or_email: PhoneOrEmailRegex