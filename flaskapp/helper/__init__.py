import hashlib
from datetime import datetime
import re

from constants import PHONE_VALIDATION,EMAIL_VALIDATION

def password_hash(password):
    """SHA256 hasf function used to hash passwords
    """
    hash = hashlib.sha256(password.encode())
    return hash.hexdigest()

def hashcompare(hash1,hash2):
    """This function will compare the given two hash and return True is match elase False
    """    
    return hash1 == hash2

def get_current_timestamp():
    """This function returns a timestamp
    """    
    curr_dt = datetime.now()
    timestamp = int(round(curr_dt.timestamp()))
    return timestamp

def is_phone(string):
    """This funtion return True if the given string is a phone number else False
    """    
    return re.match(PHONE_VALIDATION,string) and True

def is_email(string):
    """This funtion return True if the given string is a email else False
    """    
    return re.match(EMAIL_VALIDATION,string) and True