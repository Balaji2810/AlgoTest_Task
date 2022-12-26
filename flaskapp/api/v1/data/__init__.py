from flask import Blueprint,g
from flask_pydantic import validate

from .schema import SCHEMA,expects_json
from auth import generate_token,verify_token,refresh_token_required,access_token_required
from helper.formatter import ResponseModel
from mongoDbConnector import store_leg,all_leg,one_leg


data = Blueprint('data', __name__,url_prefix='/data')



@data.route('/',methods=["POST"])
@validate()
@expects_json
@access_token_required
def store_data(user_id,data):
    store_leg(user_id,data)
    return ResponseModel(data={})

@data.route('/<id>',methods=["GET"])
@validate()
@access_token_required
def get_one_data(user_id,id):
    result = one_leg(user_id,id)
    return ResponseModel(data={"leg":result})

@data.route('/',methods=["GET"])
@validate()
@access_token_required
def get_all_data(user_id):
    result = all_leg(user_id)
    return ResponseModel(data={"leg":result})