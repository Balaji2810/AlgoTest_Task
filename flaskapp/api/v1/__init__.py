from flask import Blueprint

from api.v1.user import user
from api.v1.otp_verify import otp
from api.v1.token import token
from api.v1.data import data

v1  = Blueprint('v1', __name__,url_prefix='/v1')

v1.register_blueprint(user)
v1.register_blueprint(otp)
v1.register_blueprint(data)
v1.register_blueprint(token)