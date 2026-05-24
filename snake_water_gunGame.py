import random
computer = random.choice([1,-1,0])

myInput = input("Enter your choice: ")
choiceDic = {"s":1,"w":-1,"g":0}
reverseDic = {1:"snake",-1:"water",0:"gun"}


myChoice = choiceDic[myInput]
print(f"Your choice is {reverseDic[myChoice]}\nComputer Choice is {reverseDic[computer]}")

if(reverseDic[myChoice] == reverseDic[computer]):
    print("It is Draw")
else:
    if(myChoice == 1 and computer == -1):
        print("You Wonn!")
    elif(myChoice == 1 and computer == 0):
        print("You Lost!")
    elif(myChoice == -1 and computer == 0):
        print("You Wonn!")
    elif(myChoice == -1 and computer == 1):
        print("You Lost!")
    elif(myChoice == 0 and computer == -1):
        print("You Lost!")
    elif(myChoice == 0 and computer == 1):
        print("You Wonn!")
    else:
        print("something went wrong!!")