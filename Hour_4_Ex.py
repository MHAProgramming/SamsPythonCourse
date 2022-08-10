email = 'To Whom it may Concern, \nThis is an email string example and is using \nthe word blank in the words that is required for it.  \nKind Regards, \nHaroun Azizi'
emergency = 'Do you want to make this email urgent?'
joke = 'Do you want to set this email as non-urgent?'
notification = ' '

if email.find('emergency') > 0:
    notification = emergency
elif email.find('joke') > 0:
    notification = joke
else:
    print ' '


print email
print '*'*60
print notification
print '*'*60




