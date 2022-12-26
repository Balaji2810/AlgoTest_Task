import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from helper import logger
import os

from constants import EMAIL_OTP_TEMPLATE,EMAIL_TITLE,SMTP_SERVER,SMTP_SERVER_PORT
from mongoDbConnector import generate_email_otp,verify_email_otp,check_email_not_in_db

def send_otp(recipient):
    """This function is used to send the OTP to the specified email

    Args:
        email (str): Contains the phone email

    Returns:
        [bool]: True if OTP sent sucessfully, else False
    """
    try:
        username = os.environ["mail_id"]
        password = os.environ["mail_password"]
        msg = MIMEMultipart('mixed')

        sender = os.environ["mail_id"]

        msg['Subject'] = EMAIL_TITLE
        msg['From'] = sender
        msg['To'] = recipient


        otp = generate_email_otp(recipient)
        text_message = MIMEText(EMAIL_OTP_TEMPLATE.format(otp))
        msg.attach(text_message)

        mailServer = smtplib.SMTP(SMTP_SERVER, SMTP_SERVER_PORT)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(sender, recipient, msg.as_string())
        mailServer.close()
        return True
    except Exception as e:
        logger.error(e)
        return False


def verify_otp(email, otp):
    """This function is used to verifiy the OTP

    Args:
        email (str): Contains the phone email
        otp (str): contains the OTP

    Returns:
        [bool]: True if OTP verified sucessfully, else False
    """
    try:
        status = verify_email_otp(email,otp)
        logger.info("Verify OTP "+ email+":"+ str(status))
        return status
        # return verification_check.status == "approved"
    except Exception as e:
        logger.error(e)
        return False
