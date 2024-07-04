def customer_serial(customer)->dict:
    return {
        "id" : str(customer["_id"]),
        "cust_id":str,
        "first_name" : customer["first_name"],
        "last_name" : customer["last_name"],
        "email" : customer["email"],
        "dob" : customer["dob"],
        "gender" : customer["gender"],
        "password" : customer["password"],
    }

def list_serial(cutomers)->list:
    return([customer_serial(customer) for customer in cutomers])