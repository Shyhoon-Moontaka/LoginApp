import digital_journey
import random
from datetime import datetime
object={}
def registrationData(userName,password,emailAddress):
    if userName=="" or password=="" or emailAddress=="":
        return "Registration Failed."
    else:
        id=int(random.random()*10000000000)
        date=datetime.now().isoformat()
        object[emailAddress]={
            "Id":id,
            "Username":userName,
            "Password":password,
            "Date":date
        }
        return "Registration Successful."