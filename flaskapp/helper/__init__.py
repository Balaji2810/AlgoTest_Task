import hashlib
from datetime import datetime
import re

from constants import PHONE_VALIDATION,EMAIL_VALIDATION

def password_hash(password):
    hash = hashlib.sha256(password.encode())
    return hash.hexdigest()

def hashcompare(hash1,hash2):
    return hash1 == hash2

def get_current_timestamp():
    curr_dt = datetime.now()
    timestamp = int(round(curr_dt.timestamp()))
    return timestamp

def is_phone(string):
    return re.match(PHONE_VALIDATION,string) and True

def is_email(string):
    return re.match(EMAIL_VALIDATION,string) and True