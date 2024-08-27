from random import randint
from time import sleep
import math 
tries=0
r=randint(1,1000)
circlex=randint(-5000,5000)
circley=randint(-5000,5000)
error=0
def move_circle():
    circlex=randint(-5000,5000)
    circley=randint(-5000,5000)

while(1):
    game=1
    sleep(1)
    print("a circle has appeared! can you guess where?")
    sleep(1)
    while(game):
        x=0
        y=0
        while(1):
            try:
                x = int(input("guess x value: "))
                break
            except ValueError:
                print("that's not a integer")
        while(1):     
            try:
                y = int(input("guess y value: "))
                break
            except ValueError:
                print("that's not a integer")
        if y=="": y=0
        if x=="": x=0
        error = int(math.sqrt((int(x)-circlex)**2 + (int(y)-circley)**2) - r)
        
        if error<0:
            error *=-1
        if((int(x) - circlex)**2 + (int(y) - circley)**2 < r**2):
            print("you guessed a point correctly with " + str(tries+1) + " attempt(s)! the circle had a radius of " + str(r) + " and a center of "+str(circlex)+","+str(circley))
            move_circle()
            tries=0
            game=0
        else:
            print("around " + str(error+randint(-100,100))+" units off, try again")
            tries +=1
            if tries>200:
                print("alright dum dum, i've had enough.")
                sleep(5)
                print("the circle had a center of " +str(circlex) + "," + str(circley) + " and a radius of " + str(r))
                move_circle()
                tries=0
                game=0
                
            if tries>15:
                if input("give up and reveal the location? (yes/no): ")=="yes":
                    print("you gave up, cause you're a dummy! the circle had a center of " + str(circlex) + "," + str(circley) + " and a radius of " + str(r))
                    move_circle()
                    tries=0
                    game=0

