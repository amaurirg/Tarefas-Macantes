#! python3
#Envia mensagens SMS para celulares.

from twilio.rest import TwilioRestClient

accountSID = 'ACf005356c395e3e7c76f986e9141f12c6'
authToken = '8e75013120a1d52a4a2133aa7934f4d2'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+554139087781'
myCellPhone = '+5511966315686'
message = twilioCli.messages.create(body='Envio Teste de Mensagem SMS com Python', from_=myTwilioNumber, to=myCellPhone)