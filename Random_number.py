import random
loop = True
while loop:
    max = input("enter upper limit number: ")
    if max.isdigit():
        max = int(max)

    ep_no = random.randint(1,max+1)
    print(ep_no)
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