from random import randint
tries=0
r=randint(-1000,1000)
h=randint(-5000,5000)
k=randint(-5000,5000)
error=0
def move_circle();
    h=randint(-5000,5000)
    k=randint(-5000,5000)

while(1):
    sleep(1)
    print("a circle has appeared! can you guess where?")
    sleep(1)
    x=input("guess x value: ")
    y=input("guess y value: ")
    if y=="": y=0
    if x=="": x=0
    check = (int(x)-h)*2 + (int(y)-k)*2
    if(check<0):
        error = r*2 - (check * -1)
    else:
        error = r*2 - check
    if(check<r*2 and check>0):
        print("you guessed a point correctly after "+str(tries+1)+" attempt(s)! the circle had a radius of " + str(r) + " and a center of "+str(h)+","+str(k))
        move_circle()
        tries=0
    else:
        print("around " + str(error+randint(-100,100))+" units off, try again")
        tries +=1
        if tries>200:
            print("alright dum dum, i've had enough.")
            sleep(5)
            print("the circle had a center of " +str(h) + "," + str(k)" and a radius of " + str(r))

        if tries>15:
            if input("give up and reveal the location? (yes/no): ")=="yes":
                print("you gave up, cause you're a dummy! the circle had a center of " +str(h) + "," + str(k)" and a radius of " + str(r))
                move_circle()
                tries=0
