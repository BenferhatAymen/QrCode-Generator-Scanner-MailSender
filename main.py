import json 
from QrGenerator import generate
from Sendmail import sendQr

with open("db/mails.json",encoding="UTF-8") as f:
    mails = json.load(f)
mails.setdefault("mails",{})
participants = mails["mails"].keys()
participantsList = [participant for participant in participants]

for i in participantsList:
    generate(i)
    sendQr(i)