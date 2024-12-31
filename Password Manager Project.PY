#project 03

from cryptography.fernet import Fernet

# key=Fernet.generate_key()

# print(key)

# with open("key.key","wb") as file:
#     file_key=file.write(key)

#     print(file_key)


def key_load():
    f=open("key.key",'rb')
    key = f.read()
    f.close()
    return key

key=key_load()
fer=Fernet(key)

def view():
    with open('myfile.txt','r') as file_view:
        for line in file_view.readlines():
            data=line.rstrip()
            user,passw = data.split("|")
            print("user:",user ,"| password:",fer.decrypt(passw.encode()).decode())

def add():
    name=input("enter account name: ")
    passwrod = input("enter your password: ")
    with open("myfile.txt",'a') as file_add:
        file_add.write(name+"|"+fer.encrypt(passwrod.encode()).decode()+"\n")


while True:
    mode=input("would you like to add a new password or view or q to quit").rstrip().lower()

    if mode == "q" :
        break

    if mode == "add":
        add()

    elif mode == "view":
        view()

    else:
        print("invaild option")        