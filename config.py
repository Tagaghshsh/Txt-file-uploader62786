import os

API_ID = API_ID = 23442389

API_HASH = os.environ.get("API_HASH", "70490ec8a810932cb5cb7f9d6a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6635304109:AAHw06dprDY_uux2eJn6XAJyYFjh9jvL1Hg")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 54486))

LOG = -1001974

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "544864").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


