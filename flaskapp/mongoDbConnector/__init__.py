import pymongo
from pymongo import MongoClient
import os
from random import randrange
from helper import get_current_timestamp,hashcompare,password_hash
import uuid

from helper import logger

def get_db():
    """This function returns a mongodb connection
    """    
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
    """This function will generate a OTP for email and saves the same in the mongoDB
    """    
    try:
        db = get_db()
        otp = db.otp_tb.find_one({"email":email})
        if otp == None:
            logger.info("Generating OTP for "+email)
            otp = str(randrange(100000, 1000000)) #6 digit OTP
            db["otp_tb"].insert_one({"email":email,"otp":otp})
        else:
            otp = otp["otp"] #if OTP present in the DB will send the same
        return otp
    except Exception as e:
        logger.error(e)
        raise Exception('Unable to Generate OTP for email!!!')

def verify_email_otp(email,otp):
    """This function will verify the OTP
    """    
    try:
        db = get_db()
        data = db.otp_tb.find_one({"email":email})
        print(data==None)
        if data==None:
            return False
        else:     
            if str(data["otp"]).strip() == otp.strip():
                db.otp_tb.delete_one({"email":email}) #OTP will be deleted once verified
                return True
            else:
                return False
    except Exception as e:
        logger.error(e)
        raise Exception('Unable to Generate OTP for email!!!')

def check_email_not_in_db(email):
    """This function will return True is the email is not present in the Database else False
    """    
    try:
        db = get_db()
        data = db.user.find_one({"email":email})
        if data==None:
            return True
        return False
    except Exception as e:
        logger.error(e)

def check_phone_not_in_db(phone):
    """This function will return True is the phone is not present in the Database else False
    """ 
    try:
        db = get_db()
        data = db.user.find_one({"phone":phone})
        if data==None:
            return True
        return False
    except Exception as e:
        logger.error(e)

def user_signup(email,phone,name,hash):
    """This function will create a new user based on the below details

    Args:
        email 
        phone 
        name 
        hash 
    """    
    try:
        db = get_db()
        id = db["user"].insert_one({"email":email,"phone":phone,"name":name,"password_hash":hash,"timestamp":get_current_timestamp(),"_id":uuid.uuid4().hex})
        return id.inserted_id
    except Exception as e:
        logger.error(e)

def user_login(phone_or_email,password):
    """This funtion will check if the user is regestered in the database or not.
    """    
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
    """This function will change the user pasword after verifying the phone number or email
    """    
    try:
        db = get_db()
        hash = password_hash(new_password)
        db.user.update_one({ "$or": [ { "email": phone_or_email }, { "phone": phone_or_email} ] },{"$set":{"password_hash":hash,"timestamp":get_current_timestamp()}})
    except Exception as e:
        logger.error(e)


def store_leg(user_id,data):
    """Stores the list of legs in the data base
    """    
    try:
        db = get_db()
        for records in data:
            records["_id"] = uuid.uuid4().hex
            records["user_id"] = user_id
            db.legs.insert_one(records)
        
    except Exception as e:
        logger.error(e)

def all_leg(user_id):
    """Get all the list of legs from the data base
    """
    try:
        db = get_db()
        legs = db.legs.find({"user_id":user_id})
        data = [ record for record in legs]

        return data
        
    except Exception as e:
        logger.error(e)

def one_leg(user_id,id):
    """Get a single record from the database
    """    
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