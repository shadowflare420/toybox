from random import randint
tries=0
r=200
h=randint(0,10000)
k=randint(0,10000)
error=0
while(1):
    x=input("guess x value: ")
    y=input("guess y value: ")
    if y=="": y=0
    if x=="": x=0
    check = (int(x)-h)*2 + (int(y)-k)*2
    if(check<0):
        error = check * -1
    else:
        error = r*2 - check
    if(check<r*2 and check>0):
        print("you guessed a point correctly after "+str(tries+1)+" attempt(s)! the circle had a radius of " + str(r) + " and a center of "+str(h)+","+str(k))
        h=randint(0,1000)
        k=randint(0,1000)
        tries=0
    else:
        print("around " + str(error+randint(0,100))+" units off, try again")
        tries +=1
        if tries>10:
            if input("reveal the answer? (yes/no): ")=="yes":
                print("you gave up! the circle had a radius of " + str(r) + " and a center of "+str(h)+","+str(k))
                h=randint(0,1000)
                k=randint(0,1000)
                tries=0
