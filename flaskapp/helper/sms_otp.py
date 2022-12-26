import os
from twilio.rest import Client
from helper import logger
from mongoDbConnector import check_phone_not_in_db


# https://www.twilio.com/docs/verify/


def send_otp(phone_number, country_code="91"):
    """This function is used to send the OTP to the specified number

    Args:
        phone_number (str): Contains the phone number
        country_code (str, optional): Country code. Defaults to "91".

    Returns:
        [bool]: True if OTP sent sucessfully, else False
    """
    try:
        client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
        verification = client.verify.services(
            os.environ["SERVICE_SID"]
        ).verifications.create(to="+" + country_code + phone_number, channel="sms")
        logger.info("OTP sent to "+"+"+country_code+" "+phone_number)
        return True

    except Exception as e:
        logger.error(e)
        return False


def verify_otp(phone_number, token, country_code="91"):
    """This function is used to verifiy the OTP

    Args:
        phone_number (str): Contains the phone number
        token (str): contains the OTP
        country_code (str, optional): Country code. Defaults to "91".

    Returns:
        [bool]: True if OTP verified sucessfully, else False
    """
    try:
        client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
        verification_check = client.verify.services(
            os.environ["SERVICE_SID"]
        ).verification_checks.create(to="+" + country_code + phone_number, code=token)
        logger.info("OTP "+"+" + country_code + phone_number+":"+ verification_check.status)
        return verification_check.status == "approved"
    except Exception as e:
        logger.error(e)
        return False
