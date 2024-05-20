import os

api_id = int(os.environ.get("API_ID", '24250238'))
api_hash = os.environ.get("API_HASH", 'cb3f118ce5553dc140127647edcf3720)
bot_token = os.environ.get("BOT_TOKEN", '5970237571:AAFfzAJuBgcAZM4myoHPw9YwYqW0ztvOvkE')


OWNER = int(os.environ.get("OWNER", '6175650047'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", '6175650047').split(',')):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
