import registration
def deleteData(userName,password):
    if userName not in registration.object:
        return "Account Deletion Failed."
    if userName in registration.object and registration.object[userName]==password:
        del registration.object[userName]
        return "Account Deletion Successful."
    else:
        return "Account Deletion Failed."