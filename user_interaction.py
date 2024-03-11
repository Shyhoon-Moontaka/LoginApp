import digital_journey
import registration_process
import emotional_journey
def userData():
    while True:
        print("Login or Registration or Delete?")
        userInput=input()
        if userInput=="Login":
            print("UserName: ")
            userName=input()
            print("Password: ")
            password=input()
            print("Email Address: ")
            emailAddress=input()
            print(digital_journey.loginData(userName,password,emailAddress))
        elif userInput=="Registration":
            print("UserName: ")
            userName=input()
            print("Password: ")
            password=input()
            print("Email Address: ")
            emailAddress=input()
            print(registration_process.registrationData(userName,password,emailAddress))
        elif userInput=="Delete":
            print("UserName: ")
            userName=input()
            print("Password: ")
            password=input()
            print("Email Address: ")
            emailAddress=input()
            print(emotional_journey.deleteData(userName,password,emailAddress))
        elif userInput=="Bid Farewell":
            break
userData()