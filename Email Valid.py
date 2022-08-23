def validEmail(email):
    l=len(email)
    dot=email.find(".") #return . position
    #print(dot)
    at=email.find("@")
    a=0
    for i in range(0,at):  #count alphabet
        if((email[i]>='a' and email[i]<='z') or (email[i]>='A' and email[i]<='Z')):
            a=a+1

    if(dot>0 and (dot-at)>0 and a>0 and (dot+1)<l):
        return True
    else:
        return False



while(True):
    email = input("Enter an Email address: ")
    check = validEmail(email)
    if (check == True):
        print("Valid")
    else:
        print("Ivalid")


