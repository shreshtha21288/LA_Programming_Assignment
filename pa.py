def add(a,b):                                                                 #defining a function add and two parameters a and b
    if(a==0):                                                                 #if condition that if a==0
        return b;                                                             #then return b
    if(a==1):
        if(b==0):                                                             #but if b==0
            return 1                                                          #return 1
        else:                                                                 #else
            return 0                                                          #return 0
def checksum(a,b):                                                            #defining another function checksum and passing a and b
    jam=[]                                                                    #new list called jam
    for i in range(4):                                                        #setting a range
        jam.append(add(a[i],b[i]))                                            #appending to the list
    return jam                                                                #return the list jam
def isadd(ls):                                                                #defining another function isadd
    for i in range(len(ls)):                                                  #for i in the range given
        for j in range(i,len(ls)):                                            #similarly for j in the range given
            x=ls[i]                                                           #x value
            y=ls[j]                                                           #y value
            jam=checksum(x,y)             
            if(jam in ls):                                                    #checking condition
                continue                                                      #continue the loop
            else:                                                             #otherwise
                return False                                                  #return False
    return True                                                               #return True
def mul(a,b):                                                                 #defining a function mul and two same parameters a and b
    if(a==1):                                                                 #if condition that if a==1
        return b;                                                             #then return b
    if(a==0):                                                                 #but if a==0
        return 0                                                              #then return 0
def checkmul(a,b):                                                            #defining another function checkmul and again passing a and b
    jam=[]                                                                    #new list called jam
    for i in b:                                                               #setting a range
        jam.append(mul(a,i))                                                  #again appending to the list
    return jam                                                                #return the list jam
def ismul(ls):                                                                #defining another function ismul
    for i in range(2):                                                        #for i in the range given
        for j in range(len(ls)):                                              #similarly for j in the range given
            x=ls[j]                                                           #x value
            jam=checkmul(i,x)
            if(jam in ls):                                                    #checking condition
                continue                                                      #continue the loop
            else:                                                             #otherwise
                return False                                                  #return False
    return True                                                               #return True
n=int(input("enter the dimension of the vector space:"))                      #inputting vales
ls=[]                                                                         #new list called ls
while(n>0):                                                                   #setting condition while n>0
    l=list(map(int,input("enter one space separate dimension:").split(" ")))  #entering one space separate dimension
    n=n-1;                                                                    #n=n-1
    ls.append(l)                                                              #appending the list ls
print(isadd(ls) and ismul(ls))                                                #printing and calling the functions isadd(ls) and ismul(ls)