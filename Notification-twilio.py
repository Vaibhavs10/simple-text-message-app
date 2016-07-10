# coding: utf-8

# In[1]:

accountSID = '****'
authToken = '****'
number1 = 'Your phone number'
twilio_number = '****'


# In[2]:

from twilio.rest import TwilioRestClient

def textmessage(message, no):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body = message, from_ = twilio_number, to = no)


# In[3]:

message = "Hey buddy your work's done! \n Have a nice day :)"


# In[4]:

textmessage(message, number1)
