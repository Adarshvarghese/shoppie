from fastapi import HTTPException

error_messages = {
    "email": {"errorCode": 1002, "message": "Invalid email address"},
    "password": {"errorCode": 1003, "message": "Invalid password"},
    "first_name": {"errorCode": 1004, "message": "Invalid first name"},
    "age": {"errorCode": 1005, "message": "Invalid age"},
    "dob": {"errorCode": 1006, "message": "Invalid date of birth"},
    "gender": {"errorCode": 1007, "message": "Invalid gender"},
}

def format_register_validations(errors):
    err = errors[0]
    error_field = err["loc"][-1]
    print("error filed", error_field)
    if error_field in error_messages:
        raise HTTPException(status_code=400, detail=error_messages[error_field])
    else:
        raise HTTPException(status_code=400, detail={"errorCode": 1000, "message": err["msg"]})
