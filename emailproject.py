email=input("ENTER YOUR EMAIL :  ") 
""" 
//condition - g@g.input or g@gmail.com
//1  length should be grater than 6
//2  first letter should be alphabet
//3   @ should be there and count of @ should be 1
//4   . position shold be on -3 or -4
//5   all the letters should be in lowercase and should not contain whitespace


taking three variables
 d=other than @ . _ if present
j=upper
 k=space

"""
k,j,d=0,0,0

if len(email)>=6:
    if email[0].isalpha() :
        if ("@" in email) and (email.count("@")==1):
            if(email[-3]==".") ^(email[-4]==".") :
                for i in email :
                    if i==i.isspace() :
                        k=1
                    elif i.isalpha() :
                        if i==i.upper():
                           j=1
                       
                    elif i.isdigit() :
                        continue
                    elif i=='_' or i=="@" or i=="." :
                        continue
                    else :
                        d=1
                if k==1 or j==1 or d==1 :
                    print("wrong email 5") 
                else :
                    print("right email")
            else :
                print("wrong email 4")
        else :
             print("wrong email 3")
    else :
        print("wrong email 2")
else :
    print("wrong email 1")
