# email validation checking using if else statement
email=input("Enter your email: ")
k,j,i=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if("@"in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for char in email:
                    if char==char.isspace():
                        k=1
                    elif char.isalpha():
                        if char==char.upper():
                            j=1
                    elif char.isdigit():
                        continue
                    elif char=="_" or char=="." or char=="@":
                        continue
                    else:
                        i=1
                if k==1 or j==1 or i==1:
                    print ("wrong email 5")   
                else:
                    print("right email")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1")
    
 