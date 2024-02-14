import registration
def loginData(userName,password):
    if userName not in registration.object:
        return "Login Failed! Try Again."
    if userName in registration.object and registration.object[userName]==password:
        return "Login Successful."
    else:
        return "Login Failed! Try Again."