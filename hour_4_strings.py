# In your program, you're given a string that contains the body of an email.  If the email contains
# the world "emergency," print out "Do you want to make this email urgent?" If it contains the
# word "joke," print out "Do you want to set this email as non-urgent?"



# Email Strings

# Emergency Email:  body = "Within this email is a set of text which includes an emergency within it"

# Joke Email: body = "Within this email is a set of text that has a joke within it"

# Other Email: body = "I am the rock"


# Search Operator and Text Production

body = "I am the rock"


if body.find('emergency') != -1:
    print ("Do you want to make this email urgent?")
elif body.find('joke') != -1:
    print ("Do you want to set this email as non-urgent?")
else:
    print body



