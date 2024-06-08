import os

api_id = int(os.environ.get("API_ID", '21103068'))
api_hash = os.environ.get("API_HASH", '633ab5bfab52d8763ffc6da7a9b2294a')
bot_token = os.environ.get("BOT_TOKEN", '7082937837:AAGc8hIQrWuPLHOdpBuiNhKjd5ggTdkCycM')


OWNER = int(os.environ.get("OWNER", '6286919439'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", '6286919439').split(',')):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
