import re
regexp='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regex="^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$" #more perfect

def checkEmail(mail):
    if(re.search(regexp,mail)):
        print("Valid email")
    else:
        print("Invalid Email")


while(True):
    email = input("Enter an Email address: ")
    checkEmail(email)
