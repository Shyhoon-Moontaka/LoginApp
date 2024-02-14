import login
object={}
def registrationData(userName,password):
    if userName=="" and password=="":
        return "Registration Failed."
    else:
        object[userName]=password
        return "Registration Successful."