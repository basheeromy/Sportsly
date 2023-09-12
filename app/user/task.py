"""
Tasks from user app.
"""
from app.celery import app


@app.task
def send_otp(phone, otp, *args, **kwargs):
    """
    This is an helper function to send otp to phone number
    passed as an argument to this function.

    Args:
        phone (string): mobile to send otp to.
        otp (string): otp generated in view.
    """

    if phone and otp:
        phone = str(phone)
        print(f"OTP from celery for {phone} is {otp}")
        #link = f'https://2factor.in/API/V1/{settings.OTP_API_KEY}/SMS/+91{phone}/{otp}/OTP-1' # noqa
        #result = requests.get(link, verify=False)
        #print(result)
        return "success"
    else:
        return False
