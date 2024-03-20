from cryptography.fernet import Fernet
master = input("Enter the Master Password.  ")


def view():
     with open('password.txt','r') as f :
         for line in f.readline():
             data = line.rstrip()
             user, passw = data.split("|")
             print("Username: ",user, " | Password: ", passw)


def add():
    name = input('Account Name:  ')
    pwd = input("Password:  ")

    with open('password.txt','a') as f :
        f.write(name + "|" + pwd + "\n")




while True:
    mode = input("Add a password OR View a password? (add/view), q to quit").lower()
    if mode == "q":
        break

    if mode == 'add':
        add()
    elif mode == "view":
        view()
    else:
        print("invalid option!!")
        continue