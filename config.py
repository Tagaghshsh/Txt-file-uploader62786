import os

API_ID = API_ID = 20200825

API_HASH = os.environ.get("API_HASH", "7e7f93e266c390d9cc5c2bffbe921e36")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6535968101:AAFO4BnJlqGM5-EZ_h4XO7YXufbjsdq1JQw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5008977329))

LOG = -1001907859284,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5008977329").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


