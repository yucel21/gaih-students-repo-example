# YUCEL TASKIRAN
#HOMEWORK3

sys_username = "yucel"
sys_password = "123456"
i=1

while True:
    username = input(("Username: ").lower())
    password = input("Password: ")
    if i<3:
        if sys_username == username and sys_password == password:
            print("Successful!!!\nWelcome {}".format(username))
            break
        elif sys_username != username and sys_password == password:
            print("Incorrect Username or Password \nTry Again")
            i+=1
        else:
            print("Incorrect Username or Password \nTry Again")
            i+=1
    else:
        print("Try after 30 minutes")
        break

#DICTIONARY
user = {"yucel" : "123456"}
i=1
while True:
    user1 = input(("Username: ").lower())
    password1 = input("Password: ")
    user_password = {user1 : password1}

    if i<3:
        if (user == user_password):
            print("Successful!!!\nWelcome {}".format(user1))
            break
        elif (user.keys() != user_password.keys()) and (user["yucel"] == user_password[user1]):
            print("Incorrect Password \nTry Again")
            i+=1
        else:
            print("Incorrect Username or Password \nTry Again")
            i+=1
    else:
        print("Try after 30 minutes")
        break

