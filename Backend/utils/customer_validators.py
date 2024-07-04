from fastapi import HTTPException

def format_register_validations(errors):
    err = errors[0] 
    if err["loc"][-1] == "email":
        raise HTTPException(status_code= 400,detail ={"errorCode": 1002, "message": "Invalid email address"})
    elif err["loc"][-1] == "password":
        raise HTTPException(status_code= 400,detail={"errorCode": 1003, "message": "Invalid password"})
    elif err["loc"][-1] == "first_name":
        raise HTTPException(status_code= 400,detail ={"errorCode": 1004, "message": "Invalid first name"})
    elif err["loc"][-1] == "age":
        raise HTTPException(status_code= 400,detail ={"errorCode": 1005, "message": "Invalid age"})
    elif err["loc"][-1] == "dob":
        raise HTTPException(status_code= 400,detail ={"errorCode": 1006, "message": "Invalid date of birth"})
    elif err["loc"][-1] == "gender":
        raise HTTPException(status_code= 400,detail ={"errorCode": 1007, "message": "Invalid gender"})
  
    else:
        raise HTTPException(status_code= 400,detail ={"errorCode": 1000, "message": err["msg"]})