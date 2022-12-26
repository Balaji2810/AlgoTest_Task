from flask import Blueprint
from flask_pydantic import validate

from helper.formatter import ResponseModel
from helper import logger
from helper import sms_otp,email_otp
from . model import Phone,PhoneVerify,Email,EmailVerify
from . schema import PHONE_OTP_SEND_SCHEMA


otp = Blueprint('otp', __name__,url_prefix='/otp')


@otp.route('/email',methods = ['POST'])
@validate()
def email(form:Email):
    logger.info(form.email+" sending OTP")
    status = email_otp.send_otp(form.email)
    return ResponseModel(data={"otp_sent":status})

@otp.route('/email/verify',methods = ['POST'])
@validate()
def email_verify(form:EmailVerify):
    logger.info(form.email+ " verifying the OTP")
    status = email_otp.verify_otp(form.email,form.otp)
    return ResponseModel(data={"valid_otp":status})

@otp.route('/phone/',methods = ['POST'])
@validate()
def phone(form:Phone):
    logger.info(form.phone+" sending OTP")
    status = sms_otp.send_otp(form.phone)
    
    return ResponseModel(data={"otp_sent":status})

@otp.route('/phone/verify',methods = ['POST'])
@validate()
def phone_verify(form:PhoneVerify):
    logger.info(form.phone+ " verifying the OTP")
    status = sms_otp.verify_otp(form.phone,form.otp)
    return ResponseModel(data={"valid_otp":status})