import login
import registration
import delete
def userData():
    while True:
        print("Login or Registration or Delete?")
        userInput=input()
        if userInput=="Login":
            print("UserName: ")
            userName=input()
            print("Password: ")
            password=input()
            print(login.loginData(userName,password))
        elif userInput=="Registration":
            print("UserName: ")
            userName=input()
            print("Password: ")
            password=input()
            print(registration.registrationData(userName,password))
        elif userInput=="Delete":
            print("UserName: ")
            userName=input()
            print("Password: ")
            password=input()
            print(delete.deleteData(userName,password))
        elif userInput=="END":
            break
userData()