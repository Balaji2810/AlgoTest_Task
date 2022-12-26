import jwt
import os
import datetime
from functools import wraps
from flask import request
import os

from constants import REFRESH, ACCESS,HASH,BEARER
from helper import logger
from helper.formatter import ResponseModel


def token_parser(_type,token):
    """This function will parse the JWT Token
    Args:
        _type 
        token 

    
    """    
    try:
        secret = os.environ["ACCESS_SECRET"] if _type==ACCESS else os.environ["REFRESH_SECRET"]
        payload = jwt.decode(token, secret, algorithms=[HASH])
        return payload
    except Exception as e:
        logger.error(e)
        raise Exception("Invalid Token!!")

def verify_token(_type,token):
    """This Function will verify the JWT token

    Args:
        _type 
        token 

    Returns:
        _type_:return True if Token is Valid else false
    """    
    try:
        payload = token_parser(_type,token)

        return True
    except:
        return False

def generate_token(_type,id, payload=None):
    """_summary_
    This function will generate a JWT token with the user_id in the payload
    Args:
        _type 
        id 
        payload 

    
    """    
    try:
        secret = os.environ["ACCESS_SECRET"] if _type==ACCESS else os.environ["REFRESH_SECRET"]
        if payload:
            token_payload = payload
        else:
            token_payload = {
                "user_id":id,
                "iat":datetime.datetime.utcnow()
            }
        token_payload["type"] = _type
        token = jwt.encode(token_payload, secret, algorithm=HASH)
        return token
    except Exception as e:
        logger.error(e)
        raise Exception("Token not Generated!!")


def access_token_required(f):
    """Authentication decorator

    """    
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token: # throw error if no token provided
            return ResponseModel(message="A valid token is missing!",code=401),401
        try:
           # decode the token to obtain user public_id
            bearer, token = token.split()
            if bearer != BEARER:
                return ResponseModel(message="Invalid token!",code=401),401
            data = jwt.decode(token, os.environ["ACCESS_SECRET"], algorithms=[HASH])
            user_id = data["user_id"]
        except:
            return ResponseModel(message="Invalid token!",code=401),401
         # Return the user information attached to the token
        return f(user_id=user_id, *args, **kwargs)
    return decorator

def refresh_token_required(f):
    """Authentication decorator
    """    
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token: # throw error if no token provided
            return ResponseModel(message="A valid token is missing!",code=401),401
        try:
           # decode the token to obtain user public_id
            bearer, token = token.split()
            if bearer != BEARER:
                return ResponseModel(message="Invalid token!",code=401),401
            data = jwt.decode(token, os.environ["REFRESH_SECRET"], algorithms=[HASH])
            user_id = data["user_id"]
        except:
            return ResponseModel(message="Invalid token!"),401
         # Return the user information attached to the token
        return f(user_id=user_id, *args, **kwargs)
    return decorator