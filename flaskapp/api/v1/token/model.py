from pydantic import BaseModel,constr

from constants import PASSWORD_VALIDATION,PHONE_OR_EMAIL_VALIDATION

PhoneOrEmailRegex = constr(regex=PHONE_OR_EMAIL_VALIDATION)
PasswordRegex =constr(regex=PASSWORD_VALIDATION)



class Login(BaseModel):
  phone_or_email: PhoneOrEmailRegex
  password:PasswordRegex