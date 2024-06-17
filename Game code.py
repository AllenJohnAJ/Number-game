import random as r
import sys


count=1000
x=0
y=0
name=input("enter your name")


    

def hint1():
    if i==7 or i==6:#part 1
        rt=no-25
        lt=no+25
        if rt<0:
            print("the no. is between 0 and",lt)
        elif lt>100:
            print("the no. is between",rt,"and 100")
        else:
            print("the no. is between",rt,"and",lt)

    elif i==5 or i==4:#part 2
        rt=no-20
        lt=no+20
        if rt<0:
            print("the no. is between 0 and",lt)
        elif lt>100:
            print("the no. is between",rt,"and 100")
        else:
            print("the no. is between",rt,"and",lt)
            
    elif i==3:#part 3
        rt=no-15
        lt=no+15
        if rt<0:
            print("the no. is between 0 and",lt)
        elif lt>100:
            print("the no. is between",rt,"and 100")
        else:
            print("the no. is between",rt,"and",lt)

    elif i==2:#part 4
        rt=no-10
        lt=no+10
        if rt<0:
            print("the no. is between 0 and",lt)
        elif lt>100:
            print("the no. is between",rt,"and 100")
        else:
            print("the no. is between",rt,"and",lt)

    elif i==1:#part 5
        rt=no-20
        lt=no+20
        if rt<0:
            print("the no. is between 0 and",lt)
        elif lt>100:
            print("the no. is between",rt,"and 100")
        else:
            print("the no. is between",rt,"and",lt)

def hint2():

    if no%2==0:

        print(" the no. is even")

    else:

        print("the no. is odd")

 

no=r.randint(1,100)

for i in range (7,0,-1):

    print(i,"chances left")

    a=input("enter the no. or type 'hint1' or 'hint2' for a hint")

    if a.isdigit():

        a=int(a)

        if a==no:

            print("well done")

            print("the answer was",no)

            print("your score is:",count)
            sys.exit()

        elif  a>no:

            print("high")

            count-=50

        elif  a<no:

            print("low")

            count-=50

    elif a=="hint1":

        if x==0:

            hint1()

            count-=300

            x+=1

        else:

            print("you can use hint1 only once")

    elif a=="hint2":

        if y==0:

            hint2()

            count-=200

            y+=1

        else:

            print("you can use hint2 only once")

print("you lost")

print("the answer was",no)

print("your score is:",0)

print("_________________________________________________________________________")




