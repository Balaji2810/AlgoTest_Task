import pymongo
from pymongo import MongoClient
import os
from random import randrange
from helper import get_current_timestamp,hashcompare,password_hash
import uuid

from helper import logger

def get_db():
    try:
        client = MongoClient(host='mongodb',
                            port=27017, 
                            username=os.environ["db_username"], 
                            password=os.environ["db_password"],authSource="admin")
        db = client["algotest_task"]
        return db
    except Exception as e:
        logger.error(e)
        raise Exception('MongoDB not connected!!!')


def generate_email_otp(email):
    try:
        db = get_db()
        otp = db.otp_tb.find_one({"email":email})
        if otp == None:
            logger.info("Generating OTP for "+email)
            otp = str(randrange(100000, 1000000))
            db["otp_tb"].insert_one({"email":email,"otp":otp})
        else:
            otp = otp["otp"]
        return otp
    except Exception as e:
        logger.error(e)
        raise Exception('Unable to Generate OTP for email!!!')

def verify_email_otp(email,otp):
    try:
        db = get_db()
        data = db.otp_tb.find_one({"email":email})
        print(data==None)
        if data==None:
            return False
        else:     
            if str(data["otp"]).strip() == otp.strip():
                db.otp_tb.delete_one({"email":email})
                return True
            else:
                return False
    except Exception as e:
        logger.error(e)
        raise Exception('Unable to Generate OTP for email!!!')

def check_email_not_in_db(email):
    try:
        db = get_db()
        data = db.user.find_one({"email":email})
        if data==None:
            return True
        return False
    except Exception as e:
        logger.error(e)

def check_phone_not_in_db(phone):
    try:
        db = get_db()
        data = db.user.find_one({"phone":phone})
        if data==None:
            return True
        return False
    except Exception as e:
        logger.error(e)

def user_signup(email,phone,name,hash):
    try:
        db = get_db()
        id = db["user"].insert_one({"email":email,"phone":phone,"name":name,"password_hash":hash,"timestamp":get_current_timestamp(),"_id":uuid.uuid4().hex})
        return id.inserted_id
    except Exception as e:
        logger.error(e)

def user_login(phone_or_email,password):
    try:
        db = get_db()
        data = db.user.find_one({ "$or": [ { "email": phone_or_email }, { "phone": phone_or_email} ] })
        if data==None:
            return False
        hash = password_hash(password)
        if hashcompare(hash,data["password_hash"]):
            return data["_id"]
        return False
    except Exception as e:
        logger.error(e)

def change_password(phone_or_email,new_password):
    try:
        db = get_db()
        hash = password_hash(new_password)
        db.user.update_one({ "$or": [ { "email": phone_or_email }, { "phone": phone_or_email} ] },{"$set":{"password_hash":hash,"timestamp":get_current_timestamp()}})
    except Exception as e:
        logger.error(e)


def store_leg(user_id,data):
    try:
        db = get_db()
        for records in data:
            records["_id"] = uuid.uuid4().hex
            records["user_id"] = user_id
            db.legs.insert_one(records)
        
    except Exception as e:
        logger.error(e)

def all_leg(user_id):
    try:
        db = get_db()
        legs = db.legs.find({"user_id":user_id})
        data = [ record for record in legs]

        return data
        
    except Exception as e:
        logger.error(e)

def one_leg(user_id,id):
    try:
        db = get_db()
        leg = db.legs.find_one({"$and":[{"user_id":user_id},{"_id":id}]})
        

        return leg
        
    except Exception as e:
        logger.error(e)

def get_all():
    try:
        db = get_db()
        id = db["user"].find()
        l = {}
        for i in id:
            l[i["_id"]]=i
        return l
    except Exception as e:
        logger.error(e)