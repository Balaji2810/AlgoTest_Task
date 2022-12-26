from flask import Blueprint
from flask_pydantic import validate


from . model import Login
from mongoDbConnector import user_login
from constants import ACCESS,REFRESH,INVALID_USER
from helper.formatter import ResponseModel 
from auth import generate_token,verify_token,refresh_token_required,access_token_required

token = Blueprint('token', __name__,url_prefix='/token')

@token.route('/refresh',methods=["POST"])
@validate()
def login(form:Login):
    id =  user_login(form.phone_or_email,form.password)
    if id:
        return ResponseModel(data={REFRESH:generate_token(REFRESH,id)})     
    return ResponseModel(code=401,message=INVALID_USER),401

@token.route('/access',methods=["POST"])
@validate()
@refresh_token_required
def access(user_id):
    return ResponseModel(data={ACCESS:generate_token(ACCESS,user_id)})