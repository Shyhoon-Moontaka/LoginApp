import registration_process
from datetime import datetime
def deleteData(userName,password,emailAddress):
    if emailAddress not in registration_process.object:
        return "Account Deletion Failed."
    if emailAddress in registration_process.object and registration_process.object[emailAddress]["Password"]==password and registration_process.object[emailAddress]["Username"]==userName:
        print("\nId: ",registration_process.object[emailAddress]["Id"],
            "\nUsername: ",registration_process.object[emailAddress]["Username"],
            "\nAccount Deletion Date: ",datetime.now().isoformat(),"\n"
            )
        del registration_process.object[emailAddress]
        return "Account Deletion Successful."
    else:
        return "Account Deletion Failed."