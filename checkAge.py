a = int(input("Enter your age: "))

if(a>=18):
    print("You are eligible for vote")

elif(a<18 and a>12):
    print("You are in teenage")

else:
    print("You are not eligible for vote")