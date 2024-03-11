import registration_process
data={}
def loginData(userName,password,emailAddress):
    if emailAddress not in registration_process.object:
        return "Login Failed! Try Again."
    if emailAddress in registration_process.object and registration_process.object[emailAddress]["Password"]==password and registration_process.object[emailAddress]["Username"]==userName:   
        print("\nId: ",registration_process.object[emailAddress]["Id"],
            "\nUsername: ",registration_process.object[emailAddress]["Username"],
            "\nPassword: ",registration_process.object[emailAddress]["Password"],
            "\nRegistration Date: ",registration_process.object[emailAddress]["Date"],"\n"
            )
    else:
        return "Login Failed! Try Again."