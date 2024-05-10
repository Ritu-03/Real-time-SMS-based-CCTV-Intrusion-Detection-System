from twilio.rest import Client

account_sid = 'ACf489071ce1d9338ff73b88dca1c33886'
auth_token = '491fa4b211692f0599efcaaad97a4fb8'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='+12062586195',
    body='CCTV Alert ',
    to='+919165013670'
    )

    print(message.sid)