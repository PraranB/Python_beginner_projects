import random
loop = True
while loop:
    max = input("enter upper limit number: ")
    if max.isdigit():
        max = int(max)

    Num = random.randint(1,max+1)
    print(Num)
    "\n"
    again = input("generate again? (y/n):  ").lower()
    if again == "y":
        continue
    elif again == 'n':
        loop = False
    else:
        print("ERROR!!")
        quit()

print('BYE :) ')
