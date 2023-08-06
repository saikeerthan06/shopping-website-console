#this is a seperate file to test out if we are able to send SMS through Python 
from twilio.rest import Client
import random

#Generates a 5 digit OTP.
def generate_otp():
  otp = ""
  for i in range(5):
     otp += str(random.randint(0, 9))
  return otp


def sending_OTP():
    #using an API called Twilio, we are able to send SMS through Python Code. Twilio provides us with an Acccount SID and an Authentication Key 
    #to confirm that it is us who is accessing the services. 
    #in order for Twilio to work we had to pip/pip3 install twilio into Python's terminal. 

    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = 'AC5d3a355c4c211259e28ee6947c1eaa8d'
    auth_token = 'a346d958eea4c16f7e4eac3a6fd61a9e'

    client = Client(account_sid, auth_token)

    ''' Change the value of 'from' with the number 
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''

    otp = generate_otp()
    message = client.messages.create(
        from_='+17657911854',   #twilio's number, where the message comes from 
        body= f"OTP is {otp}" ,  #what the message should say
        to= "+6581838924"   #the receiver's phone number, if you place your number inside it should send you an SMS. 
                            #pls note you should not have any anti-scam systems installed on your phone as messages from Twilio are marked as scam/spam.
    )

    return otp


def sending_confirmation(amt, credit_card, class_ask):
    #using an API called Twilio, we are able to send SMS through Python Code. Twilio provides us with an Acccount SID and an Authentication Key 
    #to confirm that it is us who is accessing the services. 
    #in order for Twilio to work we had to pip/pip3 install twilio into Python's terminal. 

    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = 'AC5d3a355c4c211259e28ee6947c1eaa8d'
    auth_token = 'a346d958eea4c16f7e4eac3a6fd61a9e'

    client = Client(account_sid, auth_token)

    ''' Change the value of 'from' with the number 
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''

    message = client.messages.create(
        from_='+17657911854',   #twilio's number, where the message comes from 
        body= f"Greetings from Gundam Store! ${amt} has been charged to credit card number ending with {credit_card[-4:]}! Thank You for choosing {class_ask} Membership!" ,  #what the message should say
        to= "+6581838924"   #the receiver's phone number, if you place your number inside it should send you an SMS. 
                            #pls note you should not have any anti-scam systems installed on your phone as messages from Twilio are marked as scam/spam.
    )




