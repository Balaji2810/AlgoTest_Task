from flask import Blueprint
from flask_pydantic import validate

from . model import SignUp,Login,ForgetPassword,Check
from mongoDbConnector import check_phone_not_in_db,check_email_not_in_db,user_signup,user_login,get_all,change_password
from helper.formatter import ResponseModel
from constants import ALREADY_PRESENT,PHONE,EMAIL,OTP,OTP_INVALID,INVALID_USER
from helper import email_otp,sms_otp,password_hash,is_email,is_phone,logger


user = Blueprint('user', __name__,url_prefix='/user')


@user.route('/signup',methods=["POST"])
@validate()
def signup(form:SignUp):
    if not check_email_not_in_db(form.email):
        return ResponseModel(code=400,message=ALREADY_PRESENT.format(EMAIL),data={"type":EMAIL}),400
    if not check_phone_not_in_db(form.phone):
        return ResponseModel(code=400,message=ALREADY_PRESENT.format(PHONE),data={"type":PHONE}),400
    email_otp_status = email_otp.verify_otp(form.email,form.email_otp)
    sms_otp_status = sms_otp.verify_otp(form.phone,form.phone_otp)
    if not email_otp_status or not sms_otp_status:
        return ResponseModel(code=400,message=OTP_INVALID,data={"type":OTP}),400
    hash = password_hash(form.password)
    id = user_signup(form.email,form.phone,form.name,hash)
    return ResponseModel(data={"id":id})



@user.route('/password',methods=["PUT"])
@validate()
def forget_password(form:ForgetPassword):
    if is_phone(form.phone_or_email):
        logger.info("OTP via SMS")
        valid_otp = sms_otp.verify_otp(form.phone_or_email,form.otp)
    else:
        logger.info("OTP via Email")
        valid_otp = email_otp.verify_otp(form.phone_or_email,form.otp)
    
    if valid_otp:
        change_password(form.phone_or_email,form.new_password)    
        return ResponseModel()
    else: 
        return ResponseModel(code=401,message=OTP_INVALID),401

@user.route('/check',methods=["POST"])
@validate()
def check(form:Check):
    
    if is_email(form.phone_or_email):
        status = not check_email_not_in_db(form.phone_or_email)
    else:
        status = not check_phone_not_in_db(form.phone_or_email)
    return ResponseModel(data={"user_present":status})


